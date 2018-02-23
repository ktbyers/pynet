#!/usr/bin/env python
"""
Optional, connect to three networking devices one after the other. Use send_command() to execute a
show command on each of these devices. Print this output to the screen.
"""
from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from getpass import getpass

password = getpass()
cisco1 = {
    'host': 'cisco.domain.com',
    'username': 'pyclass',
    'password': password,
    'device_type': 'cisco_ios',
    'command': 'show ip int brief',
}

arista1 = {
    'host': 'arista.domain.com',
    'username': 'pyclass',
    'password': password,
    'device_type': 'arista_eos',
    'command': 'show ip int brief',
}

srx1 = {
    'host': 'srx.domain.com',
    'username': 'pyclass',
    'password': password,
    'device_type': 'juniper_junos',
    'command': 'show interfaces terse'
}

for device in (cisco1, arista1, srx1):
    command = device.pop('command')
    net_connect = Netmiko(**device)
    output = net_connect.send_command(command)
    print()
    print('-' * 80)
    print("{}: {}".format(device['host'], device['device_type']))
    print(output)
    print('-' * 80)
    print()
