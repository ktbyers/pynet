#!/usr/bin/env python

'''
Create a program that opens the 'sw1_cdp.txt' file and finds all of the remote
hostnames, remote IP addresses, and remote platforms.  Your output should look 
similar to the following:

 remote_hosts: ['R1', 'R2', 'R3', 'R4', 'R5']
          IPs: ['10.1.1.1', '10.1.1.2', '10.1.1.3', '10.1.1.4', '10.1.1.5']
     platform: ['Cisco 881', 'Cisco 881', 'Cisco 881', 'Cisco 881', 'Cisco 881']

'''

import re

f = open("./CDP_DATA/sw1_cdp.txt")
cdp_data = f.read()
f.close()

tmp_dict = {}

tmp_dict['remote_hosts'] = re.findall(r"Device ID: (.+)", cdp_data)
tmp_dict['IPs'] = re.findall(r"IP address: (.+)", cdp_data)
tmp_dict['platform'] = re.findall(r"Platform: (.+?),", cdp_data)


# Print output
print 
field_order = ('remote_hosts', 'IPs', 'platform')
for k in field_order:
    print "%15s: %-20s" % (k, tmp_dict[k])

print 

