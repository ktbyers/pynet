#!/usr/bin/env python
'''
Exercise using Juniper's PyEZ to make changes to device in various ways

Using the PyEZ load method set the hostname on the device using set, conf, and XML formats.

Display the differences between the running config and candidate config after each change.
Perform at least one commit and one rollback(0) during this process.

The hostname at the end of the testing should be: pynet-jnpr-srx1
'''

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from getpass import getpass


def main():
    '''
    Exercise using Juniper's PyEZ to make changes to device in various ways
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

    cfg = Config(a_device)

    print "Setting hostname using set notation"
    cfg.load("set system host-name test1", format="set", merge=True)

    print "Current config differences: "
    print cfg.diff()

    print "Performing rollback"
    cfg.rollback(0)

    print "\nSetting hostname using {} notation (external file)"
    cfg.load(path="load_hostname.conf", format="text", merge=True)

    print "Current config differences: "
    print cfg.diff()

    print "Performing commit"
    cfg.commit()

    print "\nSetting hostname using XML (external file)"
    cfg.load(path="load_hostname.xml", format="xml", merge=True)

    print "Current config differences: "
    print cfg.diff()

    print "Performing commit"
    cfg.commit()
    print


if __name__ == "__main__":
    main()
