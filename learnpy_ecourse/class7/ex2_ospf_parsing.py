#!/usr/bin/env python

'''
Open the ./OSPF_DATA/ospf_single_interface.txt and extract the interface, IP 
address, area, type, cost, hello timer, and dead timer.  Use regular expressions 
to accomplish your extraction.

Your output should look similar to the following:

Int:    GigabitEthernet0/1
IP:     172.16.13.150/29
Area:   30395
Type:   BROADCAST
Cost:   1
Hello:  10
Dead:   40

'''

import re

f = open('./OSPF_DATA/ospf_single_interface.txt')

ospf_dict = {}

for line in f:

    intf = re.search(r"^(.+) is up, line protocol is up", line)
    if intf:
        ospf_dict['Int'] = intf.group(1)

    ip_addr = re.search(r"Internet Address (.+), Area (.+), Attached", line)
    if ip_addr:
        ospf_dict['IP'] = ip_addr.group(1)
        ospf_dict['Area'] = ip_addr.group(2)

    network_type = re.search(r", Network Type (.+), Cost: (.+)", line)
    if network_type:
        ospf_dict['Type'] = network_type.group(1)
        ospf_dict['Cost'] = network_type.group(2)

    ospf_timers = re.search(r"Timer intervals configured, Hello (.+), Dead (.+?),", line)
    if ospf_timers:
        ospf_dict['Hello'] = ospf_timers.group(1)
        ospf_dict['Dead'] = ospf_timers.group(2)


# Print output
print 
field_order = ('Int', 'IP', 'Area', 'Type', 'Hello', 'Dead')
for k in field_order:
    print "%10s: %-20s" % (k, ospf_dict[k])
print 

