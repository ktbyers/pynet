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

file_name = "show_ver.out"
net_connect = ConnectHandler(**device)
output = net_connect.send_command_expect('show version')

# Write file
with open(file_name, "w") as f:
    f.write(output)

# Read file
new_output = ''
with open(file_name) as f:
    new_output = f.read()
