#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

ip_address = raw_input("Enter IP address: ")

device = {
    'device_type': 'cisco_ios',
    'ip': ip_address,
    'username': 'pyclass',
    'password': getpass(),
    'port': 22,
} 

net_connect = ConnectHandler(**device)
output = net_connect.send_command_expect('show version')
print output
