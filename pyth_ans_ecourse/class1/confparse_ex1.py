#!/usr/bin/env python
'''
Use CiscoConfParse to find all lines starting with 'crypto map CRYPTO'

print out line and all children of line
'''

from ciscoconfparse import CiscoConfParse

def main():
    '''
    Use CiscoConfParse to find all lines starting with 'crypto map CRYPTO'

    print out line and all children of line
    '''
    cisco_file = 'cisco_ipsec.txt'

    cisco_cfg = CiscoConfParse(cisco_file)
    crypto_maps = cisco_cfg.find_objects(r"^crypto map CRYPTO")

    for c_map in crypto_maps:
        print
        print c_map.text
        for child in c_map.children:
            print child.text
    print

if __name__ == "__main__":
    main()
