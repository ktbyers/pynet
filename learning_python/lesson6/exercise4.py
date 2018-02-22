#!/usr/bin/env python
"""
Use send_config_set() and send_config_from_file() to make configuration changes.

The configuration changes should be benign. For example, on Cisco IOS I typically change the
logging buffer size.

As part of your program verify that the configuration change occurred properly. For example, use
send_command() to execute 'show run' and verify the new configuration.
"""
from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from getpass import getpass


def output_printer(output):
    print()
    print('-' * 80)
    print(output)
    print('-' * 80)
    print()


try:
    host = raw_input("Enter host to connect to: ")
except NameError:
    host = input("Enter host to connect to: ")

password = getpass()
device = {
    'host': host,
    'username': 'pyclass',
    'password': password,
    'device_type': 'cisco_ios',
}

net_connect = Netmiko(**device)

# Use send_config_set() to make config change
config = ['logging console', 'logging buffer 15000']
output = net_connect.send_config_set(config)
output_printer(output)

# Use send_config_from_file() to make config change
output = net_connect.send_config_from_file('config.txt')
output_printer(output)


message = "Verifying config change\n"
output = net_connect.send_command("show run | inc logging")
if '8000' in output:
    message += "Logging buffer is size 8000"
else:
    message += "Logging buffer size is not correct!"
output_printer(message)
