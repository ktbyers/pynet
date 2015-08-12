#!/usr/bin/env python
'''
Using SNMPv3 create a script that detects router configuration changes.

If the running configuration has changed, then send an email notification to
yourself identifying the router that changed and the time that it changed.

In this exercise, you will possibly need to save data to an external file. Use
either JSON or YAML to save the data to an external file.
'''

import os.path
from datetime import datetime
from getpass import getpass

import cPickle as pickle
import yaml
import json

from collections import namedtuple

from snmp_helper import snmp_get_oid_v3, snmp_extract
from email_helper import send_mail


# Constants
DEBUG = True

# 300 seconds (converted to hundredths of seconds)
RELOAD_WINDOW = 300 * 100

# Uptime when running config last changed
RUN_LAST_CHANGED = '1.3.6.1.4.1.9.9.43.1.1.1.0'

# Relevant SNMP OIDs
SYS_NAME = '1.3.6.1.2.1.1.5.0'
SYS_UPTIME = '1.3.6.1.2.1.1.3.0'

# Create namedtuple for network devices
NetworkDevice = namedtuple("NetworkDevice", "uptime last_changed run_config_changed")


def obtain_saved_objects(file_name):
    '''
    Read in previously saved objects from a file

    Determine from the file_name whether .pkl, .yml, or .json, properly retrieve the data from
    the file.

    Return the retrieved network devices
    '''

    net_devices = {}

    # Check that the file exists
    if not  os.path.isfile(file_name):
        return {}

    # Determine whether .pkl, .yml, or .json file
    if file_name.count(".") == 1:
        _, out_format = file_name.split(".")
    else:
        raise ValueError("Invalid file name: {0}".format(file_name))

    if out_format == 'pkl':
        with open(file_name, 'r') as f:
            while True:
                try:
                    net_devices = pickle.load(f)
                except EOFError:
                    break
    elif out_format == 'yml':
        with open(file_name, 'r') as f:
            net_devices = yaml.load(f)
    elif out_format == 'json':
        with open(file_name, 'r') as f:
            net_devices = json.load(f)

            # JSON returns straight tuple, convert to namedtuple
            for device_name, device_attrs in net_devices.items():
                uptime, last_changed, run_config_changed = device_attrs
                tmp_device = NetworkDevice(uptime, last_changed, run_config_changed)
                net_devices[device_name] = tmp_device
    else:
        raise ValueError("Invalid file name: {0}".format(file_name))

    return net_devices


def save_objects_to_file(file_name, data_dict):
    '''
    Write the network devices out to a file
    '''

    # Determine whether .pkl, .yml, or .json file
    if file_name.count(".") == 1:
        _, out_format = file_name.split(".")
    else:
        raise ValueError("Invalid file name: {0}".format(file_name))

    if out_format == 'pkl':
        with open(file_name, 'w') as f:
            pickle.dump(data_dict, f)
    elif out_format == 'yml':
        with open(file_name, 'w') as f:
            f.write(yaml.dump(data_dict, default_flow_style=False))
    elif out_format == 'json':
        with open(file_name, 'w') as f:
            json.dump(data_dict, f)


def send_notification(device_name):
    '''
    Send email notification regarding modified device
    '''

    current_time = datetime.now()

    sender = 'sender@twb-tech.com'
    recipient = 'recipient@twb-tech.com'
    subject = 'Device {0} was modified'.format(device_name)

    message = '''
The running configuration of {0} was modified.  

This change was detected at: {1}

'''.format(device_name, current_time)

    if send_mail(recipient, subject, message, sender):
        print 'Email notification sent to {}'.format(recipient)
        return True


def main():
    '''
    Check if the running-configuration has changed, send an email notification when
    this occurs.

    Logic for detecting the running-config has changed:

        Normal (non-reboot):

            # Did RUN_LAST_CHANGED increase
            if RUN_LAST_CHANGED > network_device_object.last_changed:
                config_changed = True

        Reboot case:

            RUN_LAST_CHANGED decreases (i.e. < network_device_object.last_changed)

            Right after reboot, RUN_LAST_CHANGED is updated upon
            load of running-config from startup-config.

            Create a grace window (RELOAD_WINDOW) for values of RUN_LAST_CHANGED.
            In other words as long as RUN_LAST_CHANGED is <= RELOAD_WINDOW assume
            no running-config changes.

            If RUN_LAST_CHANGED is > RELOAD_WINDOW assume running-config was changed
    '''

    # File for storing previous RunningLastChanged timestamp
    net_dev_file = 'netdev.pkl'     # can be .pkl, .yml, or .json
    #net_dev_file = 'netdev.yml'     # can be .pkl, .yml, or .json
    #net_dev_file = 'netdev.json'     # can be .pkl, .yml, or .json

    # SNMPv3 Connection Parameters
    ip_addr = raw_input("Enter router IP: ")
    a_user = 'pysnmp'
    my_key = getpass(prompt="Auth + Encryption Key: ")
    auth_key = my_key
    encrypt_key = my_key
    snmp_user = (a_user, auth_key, encrypt_key)
    pynet_rtr1 = (ip_addr, 7961)
    pynet_rtr2 = (ip_addr, 8061)

    print '\n*** Checking for device changes ***'

    saved_devices = obtain_saved_objects(net_dev_file)
    print "{0} devices were previously saved\n".format(len(saved_devices))

    # Temporarily store the current devices in a dictionary
    current_devices = {}

    # Connect to each device / retrieve last_changed time
    for a_device in (pynet_rtr1, pynet_rtr2):

        snmp_results = []
        for oid  in (SYS_NAME, SYS_UPTIME, RUN_LAST_CHANGED):
            snmp_results.append(snmp_extract(snmp_get_oid_v3(a_device, snmp_user, oid=oid)))

        device_name, uptime, last_changed = snmp_results

        if DEBUG:
            print "\nConnected to device = {0}".format(device_name)
            print "Last changed timestamp = {0}".format(last_changed)
            print "Uptime = {0}".format(uptime)

        # see if this device has been previously saved
        if device_name in saved_devices:

            saved_device = saved_devices[device_name]
            print "{0} {1}".format(device_name, (35 - len(device_name))*'.'),

            # Check for a reboot (did uptime decrease or last_changed decrease?)
            if uptime < saved_device.uptime or last_changed < saved_device.last_changed:

                if last_changed <= RELOAD_WINDOW:
                    print "DEVICE RELOADED...not changed"
                    current_devices[device_name] = NetworkDevice(uptime, last_changed, False)

                else:
                    print "DEVICE RELOADED...and changed"
                    current_devices[device_name] = NetworkDevice(uptime, last_changed, True)

                    send_notification(device_name)

            # running-config last_changed is the same
            elif last_changed == saved_device.last_changed:
                print "not changed"
                current_devices[device_name] = NetworkDevice(uptime, last_changed, False)

            # running-config was modified
            elif last_changed > saved_device.last_changed:
                print "CHANGED"
                current_devices[device_name] = NetworkDevice(uptime, last_changed, True)
                send_notification(device_name)

            else:
                raise ValueError()

        else:
            # New device, just save it
            print "{0} {1}".format(device_name, (35 - len(device_name))*'.'),
            print "saving new device"
            current_devices[device_name] = NetworkDevice(uptime, last_changed, False)


    save_objects_to_file(net_dev_file, current_devices)

    print


if __name__ == '__main__':
    main()
