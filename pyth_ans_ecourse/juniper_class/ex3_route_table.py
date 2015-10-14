#!/usr/bin/env python
'''
Connect to Juniper device using PyEZ. Display the routing table.
'''

from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from getpass import getpass


def main():
    '''
    Connect to Juniper device using PyEZ. Display the routing table.
    '''
    pwd = getpass()
    ip_addr = raw_input("Enter Juniper SRX IP: ")
    ip_addr = ip_addr.strip()

    juniper_srx = {
        "host": ip_addr,
        "user": "pyclass",
        "password": pwd
    }

    print "\n\nConnecting to Juniper SRX...\n"
    a_device = Device(**juniper_srx)
    a_device.open()

    routes = RouteTable(a_device)
    routes.get()

    print "\nJuniper SRX Routing Table: "
    for a_route, route_attr in routes.items():
        print "\n" + a_route
        for attr_desc, attr_value in route_attr:
            print "  {} {}".format(attr_desc, attr_value)

    print "\n"


if __name__ == "__main__":
    main()
