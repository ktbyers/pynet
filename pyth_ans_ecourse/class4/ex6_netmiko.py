#!/usr/bin/env python
'''
Use Netmiko to execute 'show version' on pynet-rtr1 and pynet-rtr2
'''

from getpass import getpass
from netmiko import ConnectHandler
from test_devices import pynet1, pynet2, juniper_srx

def main():
    '''
    Use Netmiko to execute 'show version' on pynet-rtr1 and pynet-rtr2
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
        output = net_connect.send_command("show version")
        print
        print '#' * 80
        print "Device: {}:{}".format(net_connect.ip, net_connect.port)
        print
        print output
        print '#' * 80
        print

if __name__ == "__main__":
    main()
