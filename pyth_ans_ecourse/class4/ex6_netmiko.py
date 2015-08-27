#!/usr/bin/env python
'''
Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx
'''

from getpass import getpass
from datetime import datetime
from netmiko import ConnectHandler
from test_devices import pynet1, pynet2, juniper_srx

def main():
    '''
    Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx
    '''
    ip_addr = raw_input("Enter IP address: ")
    password = getpass()

    # Get connection parameters setup correctly
    for a_dict in (pynet1, pynet2, juniper_srx):
        a_dict['ip'] = ip_addr
        a_dict['password'] = password
        a_dict['verbose'] = False

    print "\nStart time: " + str(datetime.now())

    for a_device in (pynet1, pynet2, juniper_srx):
        net_connect = ConnectHandler(**a_device)
        output = net_connect.send_command("show arp")
        print
        print '#' * 80
        print "Device: {}:{}".format(net_connect.ip, net_connect.port)
        print
        print output
        print '#' * 80
        print

    print "\nEnd time: " + str(datetime.now())

if __name__ == "__main__":
    main()
