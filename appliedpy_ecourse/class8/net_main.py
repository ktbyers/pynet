#!/usr/bin/env python

import django
import time

from net_system.models import NetworkDevice, Credentials, SnmpCredentials

from remote_connection import SSHConnection
from inventory import CiscoGatherInventory,AristaGatherInventory


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
            pass

        elif 'eapi' in a_device.device_class:
            if DEBUG: print "eAPI inventory call: {} {}\n".format(a_device.device_name, a_device.device_class)
            pass

        else:
            # invalid condition / exception
            pass


if __name__ == "__main__":

    django.setup()

    LOOP_DELAY = 300
    VERBOSE = True

    time.sleep(3)
    print

    while True:
        
        if VERBOSE: print "### Gather inventory from devices ###"
        inventory_dispatcher()

        if VERBOSE: print "Sleeping for {} seconds".format(LOOP_DELAY)
        time.sleep(LOOP_DELAY)
        
