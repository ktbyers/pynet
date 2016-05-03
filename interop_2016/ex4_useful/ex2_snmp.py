#!/usr/bin/env python
import getpass
import snmp_helper

SYS_DESCR = '1.3.6.1.2.1.1.1.0'
SYS_NAME = '1.3.6.1.2.1.1.5.0'


def main():
    ip_addr = raw_input("IP address: ")
    ip_addr = ip_addr.strip()
    community_string = getpass.getpass(prompt="Community string: ")
    pynet_rtr1 = (ip_addr, community_string, 7961)
    pynet_rtr2 = (ip_addr, community_string, 8061)
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
