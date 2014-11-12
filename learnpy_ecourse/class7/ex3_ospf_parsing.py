#!/usr/bin/env python

'''

The file 'OSPF_DATA/ospf_data.txt' contains the output from 'show ip ospf 
interface'.  Using some functions and some regular expressions, parse this 
output to display the following (note, I ended up using re.split() as part of 
the solution to this problem):

Int:    Loopback0
IP:     10.90.3.38/32
Area:   30395
Type:   LOOPBACK
Cost:   1

Int:    GigabitEthernet0/1
IP:     172.16.13.150/29
Area:   30395
Type:   BROADCAST
Cost:   1
Hello:  10
Dead:   40

Int:    GigabitEthernet0/0.2561
IP:     10.22.0.117/30
Area:   30395
Type:   POINT_TO_POINT
Cost:   1
Hello:  10
Dead:   40

'''

import re


def separate_interface_data(ospf_data):
    '''
    Take 'show ip ospf interface' data as a string

    Return a list corresponding to each section of the data
    (where a section pertains to one interface)

    ['interface1 ospf info', 'interface2 ospf info', etc ]

    '''

    # Split the data based on 'is up, line protocol is up' but retain this string
    ospf_data = re.split(r'(.+ is up, line protocol is up)', ospf_data)

    # Dump any data before the first 'is up, line protocol is up'
    ospf_data.pop(0)

    ospf_list = []

    while True:
        if len(ospf_data) >= 2:
            intf = ospf_data.pop(0)
            section = ospf_data.pop(0)

            # reunify because it was split up in the re.split
            ospf_string = intf + section
            ospf_list.append(ospf_string)

        else:
            break

    return ospf_list


def generic_ospf_parser(pattern, ospf_data):
    '''
    Takes a generic regular expression pattern that has a group(1) match 
    pattern and returns this

    Else returns None
    '''

    a_match = re.search(pattern, ospf_data)
    if a_match:
        return a_match.group(1)
    return None


def print_ospf_out(a_dict):
    '''
    Prints a given ospf interface section to STDOUT
    '''

    field_order = ('Int', 'IP', 'Area', 'Type', 'Cost', 'Hello', 'Dead')

    print
    for a_field in field_order:
        if a_dict.get(a_field) is not None:
            print "%15s:   %-20s" % (a_field, a_dict.get(a_field))
    

# Technique to allow importable and executable code to coexist (will explain in class#8)
if __name__ == '__main__':


    f = open('./OSPF_DATA/ospf_data.txt')

    ospf_data = f.read()
    ospf_data_sections = separate_interface_data(ospf_data)
    f.close()

    ospf_intf_patterns = {
        'Int'   : r"^(.+) is up, line protocol is up",
        'IP'    : r"Internet Address (.+?),",
        'Area'  : r"Internet Address .+?, Area (.+?), Attached",
        'Type'  : r", Network Type (.+?),",
        'Cost'  : r", Network Type .+?, Cost: (.+)",
        'Hello' : r"Timer intervals configured, Hello (.+?),",
        'Dead'  : r"Timer intervals configured, Hello .+?, Dead (.+?),",
    } 

    for section in ospf_data_sections:

        tmp_dict = {}
        for k,ospf_pattern in ospf_intf_patterns.items():
            return_val = generic_ospf_parser(ospf_pattern, section)
            if return_val is not None:
                tmp_dict[k] = return_val

        # Print this OSPF interface section to STDOUT
        print_ospf_out(tmp_dict)


    print
