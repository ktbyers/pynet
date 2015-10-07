#!/usr/bin/env python
'''
Connect to Juniper device using PyEZ. Display operational state and pkts_in, pkts_out for all
of the interfaces.
'''

from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable
from getpass import getpass


def main():
    '''
    Connect to Juniper device using PyEZ. Display operational state and pkts_in, pkts_out for all
    of the interfaces.
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

    eth_ports = EthPortTable(a_device)
    eth_ports.get()

    print "{:>15} {:>12} {:>12} {:>12}".format("INTF", "OPER STATE", "IN PACKETS", "OUT PACKETS")
    for intf, eth_stats in eth_ports.items():
        eth_stats = dict(eth_stats)
        oper_state = eth_stats['oper']
        pkts_in = eth_stats['rx_packets']
        pkts_out = eth_stats['tx_packets']
        print "{:>15} {:>12} {:>12} {:>12}".format(intf, oper_state, pkts_in, pkts_out)
    print


if __name__ == "__main__":
    main()
