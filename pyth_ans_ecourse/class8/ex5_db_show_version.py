#!/usr/bin/env python
'''
Use Netmiko to connect to each of the devices in the database. Execute
'show version' on each device. Record the amount of time required to do this.
'''

from netmiko import ConnectHandler
from datetime import datetime

from net_system.models import NetworkDevice
import django

def show_version(a_device):
    '''
    Execute show version command using Netmiko
    '''
    creds = a_device.credentials
    remote_conn = ConnectHandler(device_type=a_device.device_type,
                                 ip=a_device.ip_address,
                                 username=creds.username,
                                 password=creds.password,
                                 port=a_device.port, secret='')
    print
    print '#' * 80
    print remote_conn.send_command_expect("show version")
    print '#' * 80
    print

def main():
    '''
    Use Netmiko to connect to each of the devices in the database. Execute
    'show version' on each device.
    '''
    django.setup()

    start_time = datetime.now()
    devices = NetworkDevice.objects.all()
    for a_device in devices:
        show_version(a_device)

    elapsed_time = datetime.now() - start_time
    print "Elapsed time: {}".format(elapsed_time)

if __name__ == "__main__":
    main()
