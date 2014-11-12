#!/usr/bin/env python

import django
import time

from net_system.models import NetworkDevice, Credentials, SnmpCredentials

from remote_connection import SSHConnection
from inventory import CiscoGatherInventory,AristaGatherInventory
from inventory import onepk_find_model,onepk_find_device_type,onepk_find_os_version

import onepk_helper
import eapilib


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


def retrieve_config():

    CFGS_DIR = '/home/kbyers/CFGS/'

    DEBUG = True

    net_devices = NetworkDevice.objects.all()
    
    for a_device in net_devices:

        if 'ssh' in a_device.device_class:
            if DEBUG: print "Retrieve device configuration: {} {}\n".format(a_device.device_name, 
                    a_device.device_class)
            ssh_connect = SSHConnection(a_device)
            ssh_connect.enable_mode()
            output = ssh_connect.send_command('show run\n')

            file_name = a_device.device_name + '.txt'
            full_path = CFGS_DIR + file_name
            if DEBUG: print "Writing configuration file to file system\n"
            with open(full_path, 'w') as f:
                f.write(output)


if __name__ == "__main__":

    django.setup()

    LOOP_DELAY = 300
    VERBOSE = True

    time.sleep(3)
    print

    while True:
        
        if VERBOSE: print "### Gather inventory from devices ###"
        inventory_dispatcher()

        if VERBOSE: print "\n### Retrieve config from devices ###"
        retrieve_config()

        if VERBOSE: print "Sleeping for {} seconds".format(LOOP_DELAY)
        time.sleep(LOOP_DELAY)
        
