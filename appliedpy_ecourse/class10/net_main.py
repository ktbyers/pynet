#!/usr/bin/env python

import time
from datetime import datetime
from pprint import pprint
import os
import subprocess

import django
from django.utils import timezone

from net_system.models import NetworkDevice, Credentials, SnmpCredentials

from remote_connection import SSHConnection
from inventory import CiscoGatherInventory,AristaGatherInventory
from inventory import onepk_find_model,onepk_find_device_type,onepk_find_os_version
from snmp_config_detect import snmp_wrapper
from email_helper import send_mail

import onepk_helper
import eapilib

import global_params


def git_handling():

    GIT = '/bin/git'
    orig_dir = os.getcwd()

    # Change dir to CFGS_DIR
    os.chdir(global_params.CFGS_DIR)
    current_dir = os.getcwd() + '/'

    if current_dir == global_params.CFGS_DIR:

        # Perform git add
        proc = subprocess.Popen([GIT, 'add', '*.txt'], stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE)
        (std_out, std_err) = proc.communicate()

        # Perform git commit
        commit_message = "Network config changes (auto)"
        proc = subprocess.Popen([GIT, 'commit', '-m', commit_message], stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE)
        (std_out, std_err) = proc.communicate()

    # Change dir back to original directory
    os.chdir(orig_dir)


def find_diff(file1, file2):
    '''
    Find the differences between the two configuraiton files
    '''

    DEBUG = True

    DIFF = '/bin/diff'

    # Format of the first entry is an array of [COMMAND, OPTION, OPTION]
    proc = subprocess.Popen([DIFF, file1, file2], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # proc.communicate returns a tuple of (stdout, stderr)
    (diff_output, STDERR) = proc.communicate()
    if DEBUG:
        print ">>>Config differences:"
        print diff_output

    return diff_output


def print_inventory(a_device):

    fields = [
        'device_name',
        'ip_address',
        'device_class',
        'ssh_port',
        'api_port',
        'vendor',
        'model',
        'device_type',
        'os_version',
        'serial_number',
        'uptime_seconds',
    ]

    print
    print '#' * 80

    for a_field in fields:
        value = getattr(a_device, a_field)
        print "{:>15s}: {:<65s}".format(a_field, str(value))

    print '#' * 80
    print


def inventory_dispatcher():
    '''
    Dispatcher for calling SSH, onePK, or eAPI based on the 
    NetworkDevice.device_class
    '''

    DEBUG = True

    # Single location to specify the relevant GatherInventory class to use
    CLASS_MAPPER = {
        'cisco_ios_ssh'     : CiscoGatherInventory,
        'arista_eos_ssh'    : AristaGatherInventory,
    }

    net_devices = NetworkDevice.objects.all()

    for a_device in net_devices:

        if 'ssh' in a_device.device_class:
            if DEBUG: print "SSH inventory call: {} {}\n".format(a_device.device_name, a_device.device_class)
            ssh_connect = SSHConnection(a_device)
            output = ssh_connect.send_command('show version\n')
            inventory_obj = CLASS_MAPPER[a_device.device_class](a_device, output)
            
            inventory_obj.find_vendor()
            inventory_obj.find_model()
            inventory_obj.find_device_type()
            inventory_obj.find_os_version()
            inventory_obj.find_serial_number()
            inventory_obj.find_uptime()

            print 'Inventory gathering for device complete'
            print_inventory(a_device)

        elif 'onepk' in a_device.device_class:
            if DEBUG: print "onePK inventory call: {} {}\n".format(a_device.device_name, a_device.device_class)

            # FIX - pin_file is hard-coded
            onepk_connect = onepk_helper.NetworkDevice(
                ip=a_device.ip_address,
                username=a_device.credentials.username,
                password=a_device.credentials.password,
                port=a_device.api_port,
                pin_file='pynet-rtr1-pin.txt'
            )

            onepk_connect.establish_session()

            a_device.vendor = 'cisco'
            part_number = onepk_connect.net_element.properties.product_id
            a_device.model = onepk_find_model(part_number)
            a_device.device_type = onepk_find_device_type(a_device.model)
            sys_descr = onepk_connect.net_element.properties.sys_descr
            a_device.os_version = onepk_find_os_version(sys_descr)
            a_device.serial_number = onepk_connect.net_element.properties.SerialNo
            a_device.uptime_seconds = onepk_connect.net_element.properties.sys_uptime
            a_device.save()

            onepk_connect.disconnect()

            print 'Inventory gathering for device complete'
            print_inventory(a_device)

        elif 'eapi' in a_device.device_class:

            if DEBUG: print "eAPI inventory call: {} {}\n".format(a_device.device_name, a_device.device_class)

            eapi_conn = eapilib.create_connection(
                hostname = a_device.ip_address,
                username=a_device.credentials.username,
                password=a_device.credentials.password,
                port=a_device.api_port
            )

            response = eapi_conn.run_commands(['show version'])
            arista_dict = response[0]

            a_device.vendor = 'arista'
            a_device.model = arista_dict['modelName']

            # Should really be a function
            if a_device.model == 'vEOS':
                a_device.device_type = 'switch'
            else:
                a_device.device_type = ''
            a_device.os_version = arista_dict['version']

            a_device.serial_number = arista_dict['serialNumber']
            # Should normalize the MacAddress format
            if not a_device.serial_number:
                a_device.serial_number = arista_dict['systemMacAddress']

            # bootupTimestamp is since epoch. Requires time on router to be right.
            uptime_seconds = arista_dict['bootupTimestamp']
            time_delta = time.time() - int(uptime_seconds)
            a_device.uptime_seconds = int(time_delta)

            a_device.save()

            print 'Inventory gathering for device complete'
            print_inventory(a_device)

        else:
            # invalid condition / exception
            pass


def backup_config(a_device):

    DEBUG = True
    perform_diff = False

    if DEBUG: print "Retrieve device configuration via SSH: {}\n".format(a_device.device_name)
    ssh_connect = SSHConnection(a_device)
    ssh_connect.enable_mode()
    output = ssh_connect.send_command('show run\n')

    file_name = a_device.device_name + '.txt'
    full_path = global_params.CFGS_DIR + file_name
    bup_file = global_params.CFGS_DIR + a_device.device_name + '.old'

    # Check if file already exists
    if os.path.isfile(full_path):
        # Create copy of old file
        cmd_status = subprocess.call(['/bin/mv', full_path, bup_file])
        perform_diff = True

    if DEBUG: print "Writing configuration file to file system\n"
    with open(full_path, 'w') as f:
        f.write(output)

    a_device.cfg_file = file_name
    a_device.cfg_archive_time = timezone.make_aware(datetime.now(), timezone.get_current_timezone())

    # obtain last_changed time (Cisco specific)
    a_device.cfg_last_changed = int(snmp_wrapper(a_device, oid=global_params.OID_RUNNING_LAST_CHANGED))
    a_device.save()

    if perform_diff:
        return find_diff(full_path, bup_file)
    else:
        return None


def detect_config_change():

    net_devices = NetworkDevice.objects.all()

    config_changed = False
    for a_device in net_devices:

        if 'cisco' in a_device.device_class:

            # check if config file exists
            if not a_device.cfg_file:
                print "Initial device backup: {}".format(a_device.device_name)
                backup_config(a_device)
                config_changed = True
                continue

            # Check if the configuration changed
            last_changed = int(snmp_wrapper(a_device, oid=global_params.OID_RUNNING_LAST_CHANGED))
            if last_changed > a_device.cfg_last_changed:
                print ">>>Running configuration changed: {}".format(a_device.device_name)
                config_diffs = backup_config(a_device)
                config_changed = True
                if config_diffs:
                    print "Sending email notification regarding changes\n"
                    subject = "Network Device Changed: {}".format(a_device.device_name)
                    send_mail(global_params.EMAIL_RECIPIENT, subject, config_diffs, global_params.EMAIL_SENDER)
            else:
                # Update last_changed field to handle reboot case
                a_device.cfg_last_changed = last_changed
                a_device.save()

    if config_changed:
        print "Checking configuration changes into git"
        git_handling()


if __name__ == "__main__":

    django.setup()

    VERBOSE = True

    time.sleep(3)
    print

    while True:
        
        if VERBOSE: print "### Gather inventory from devices ###"
        inventory_dispatcher()

        if VERBOSE: print "\n### Detect device configuration changes ###\n"
        detect_config_change()

        if VERBOSE: print "\nSleeping for {} seconds".format(global_params.LOOP_DELAY)
        time.sleep(global_params.LOOP_DELAY)
        
