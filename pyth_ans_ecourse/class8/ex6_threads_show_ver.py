#!/usr/bin/env python
'''
Use threads and Netmiko to connect to each of the devices in the database. Execute
'show version' on each device. Record the amount of time required to do this.
'''

from netmiko import ConnectHandler
from datetime import datetime

from net_system.models import NetworkDevice
import django

import threading


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
    Use threads and Netmiko to connect to each of the devices in the database. Execute
    'show version' on each device. Record the amount of time required to do this.
    '''
    django.setup()
    start_time = datetime.now()
    devices = NetworkDevice.objects.all()

    for a_device in devices:
        my_thread = threading.Thread(target=show_version, args=(a_device,))
        my_thread.start()

    main_thread = threading.currentThread()
    for some_thread in threading.enumerate():
        if some_thread != main_thread:
            print some_thread
            some_thread.join()

    print "\nElapsed time: " + str(datetime.now() - start_time)

if __name__ == "__main__":
    main()
