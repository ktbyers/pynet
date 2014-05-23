#!/usr/bin/env python

'''
Create a program that opens the 'r1_cdp.txt' file and using regular 
expressions extracts the remote hostname, remote IP address, model, vendor, 
and device_type.
'''

import re
from pprint import pprint
from glob import glob


def generic_cdp_parser(pattern, cdp_data):
    '''
    Search for pattern in the cdp_data

    Return relevant .group(1) 
    Else return ''
    '''
 
    # Break the CDP data up into its individual lines
    cdp_data = cdp_data.split('\n')

    for line in cdp_data:
        # Search for pattern
        re_pattern = re.search(pattern, line)

        # Return match if found
        if re_pattern:
            return_val = re_pattern.group(1)
            return return_val.strip()

    return ''


# Technique to allow importable and executable code to coexist (will explain in class#8)
if __name__ == '__main__':
    
    cdp_file = 'CDP_DATA/r1_cdp.txt'
    f = open(cdp_file)
    
    # Read cdp_data into a list
    cdp_data = f.read()
    f.close()

    network_devices = {}

    network_devices['remote_hostname'] = generic_cdp_parser(r'Device ID: (.+)', cdp_data)
    network_devices['ip'] = generic_cdp_parser(r'IP address: (.+)', cdp_data)
    network_devices['vendor'] = generic_cdp_parser(r'^Platform: (.+?) ', cdp_data)
    network_devices['model'] = generic_cdp_parser(r'^Platform: \w+ (.+),', cdp_data)
    network_devices['device_type'] = generic_cdp_parser(r'^Platform: .+Capabilities: (.+?) ', cdp_data)


    print
    pprint(network_devices)
    print

