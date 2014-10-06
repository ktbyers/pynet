#!/usr/bin/env python
'''
Use Arista's eAPI to obtain 'show interfaces' from the switch.  Parse the 'show 
interfaces' output to obtain the 'inOctets' and 'outOctets' fields for each of 
the interfaces on the switch.  Accomplish this directly using jsonrpclib.
'''

import jsonrpclib
from pprint import pprint

arista_dict = dict(
    ip = '10.10.10.10',
    port = 8543,
    username = 'eapi',
    password = '*********',
)

eapi_url = 'https://{username}:{password}@{ip}:{port}/command-api'.format(**arista_dict)
eapi_conn = jsonrpclib.Server(eapi_url)

interfaces = eapi_conn.runCmds(1, ["show interfaces"])

# Strip off unneeded data structures
interfaces = interfaces[0]['interfaces']

# inOctets/outOctets are fields inside 'interfaceCounters' dict
data_stats = {}
for interface,int_values in interfaces.items():
    int_counters = int_values.get('interfaceCounters', {})
    data_stats[interface] = (int_counters.get('inOctets'), int_counters.get('outOctets'))

# Print output data
print "\n{:20} {:<20} {:<20}".format("Interface:", "inOctets", "outOctets")
for intf,octets in data_stats.items():
    print "{:20} {:<20} {:<20}".format(intf, octets[0], octets[1])

print
