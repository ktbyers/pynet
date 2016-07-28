#!/usr/bin/env python
'''
Create a script that connects to both routers (pynet-rtr1 and pynet-rtr2) and
prints out both the MIB2 sysName and sysDescr.
'''
import getpass
import snmp_helper

SYS_DESCR = '1.3.6.1.2.1.1.1.0'
SYS_NAME = '1.3.6.1.2.1.1.5.0'

def main():
    '''
    Create a script that connects to both routers (pynet-rtr1 and pynet-rtr2) and
    prints out both the MIB2 sysName and sysDescr.
    '''
    ip_addr1 = raw_input("pynet-rtr1 IP address: ")
    ip_addr2 = raw_input("pynet-rtr2 IP address: ")
    community_string = getpass.getpass(prompt="Community string: ")

    pynet_rtr1 = (ip_addr1, community_string, 161)
    pynet_rtr2 = (ip_addr2, community_string, 161)

    for a_device in (pynet_rtr1, pynet_rtr2):
        print "\n*********************"
        for the_oid in (SYS_NAME, SYS_DESCR):
            snmp_data = snmp_helper.snmp_get_oid(a_device, oid=the_oid)
            output = snmp_helper.snmp_extract(snmp_data)

            print output
        print "*********************"
    print

if __name__ == "__main__":
    main()
