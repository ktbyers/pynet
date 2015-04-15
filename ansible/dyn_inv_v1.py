#!/usr/bin/env python
'''
Ansible dynamic inventory experimentation

Output dynamic inventory as JSON from statically defined data structures
'''

import argparse
import json


ANSIBLE_INV = {
    "arista": {
        "hosts": ["pynet-sw1", "pynet-sw2", "pynet-sw3", "pynet-sw4"],
        "vars": {
            "ansible_connection": "local",
            "eapi_hostname": "10.10.10.227",
            "eapi_username": "admin1",
            "eapi_password": "password",
        }
    },
    'local': {
        'hosts': ['localhost'],
        'vars': {'ansible_connection': 'local'}
    }
}

HOST_VARS = {
    "pynet-sw1": {"eapi_port": 8243},
    "pynet-sw2": {"eapi_port": 8343},
    "pynet-sw3": {"eapi_port": 8443},
    "pynet-sw4": {"eapi_port": 8543},
}


def output_list_inventory(json_output):
    '''
    Output the --list data structure as JSON
    '''
    print json.dumps(json_output)


def find_host(search_host, inventory):
    '''
    Find the given variables for the given host and output them as JSON
    '''
    host_attribs = inventory.get(search_host, {})
    print json.dumps(host_attribs)


def main():
    '''
    Ansible dynamic inventory experimentation

    Output dynamic inventory as JSON from statically defined data structures
    '''

    # Argument parsing
    parser = argparse.ArgumentParser(description="Ansible dynamic inventory")
    parser.add_argument("--list", help="Ansible inventory of all of the groups",
                        action="store_true", dest="list_inventory")
    parser.add_argument("--host", help="Ansible inventory of a particular host", action="store",
                        dest="ansible_host", type=str)

    cli_args = parser.parse_args()
    list_inventory = cli_args.list_inventory
    ansible_host = cli_args.ansible_host

    if list_inventory:
        output_list_inventory(ANSIBLE_INV)

    if ansible_host:
        find_host(ansible_host, HOST_VARS)


if __name__ == "__main__":
    main()
