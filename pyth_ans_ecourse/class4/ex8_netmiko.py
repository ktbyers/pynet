#!/usr/bin/env python
'''
Use Netmiko to change the logging buffer size and to disable console logging
from a file for both pynet-rtr1 and pynet-rtr2

logging buffered <size>
no logging console
'''

from getpass import getpass
from netmiko import ConnectHandler
from test_devices import pynet1, pynet2, juniper_srx

def main():
    '''
    Use Netmiko to change the logging buffer size and to disable console logging
    from a file for both pynet-rtr1 and pynet-rtr2
    '''
    ip_addr = raw_input("Enter IP address: ")
    password = getpass()

    # Get connection parameters setup correctly
    for a_dict in (pynet1, pynet2, juniper_srx):
        a_dict['ip'] = ip_addr
        a_dict['password'] = password
        a_dict['verbose'] = False

    for a_device in (pynet1, pynet2):
        net_connect = ConnectHandler(**a_device)
        net_connect.send_config_from_file(config_file='config_file.txt')

        # Verify configuration
        output = net_connect.send_command("show run | inc logging")
        print
        print '#' * 80
        print "Device: {}:{}".format(net_connect.ip, net_connect.port)
        print
        print output
        print '#' * 80
        print

if __name__ == "__main__":
    main()
