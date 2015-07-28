#!/usr/bin/env python
'''
Write a Python program that creates a list. One of the elements of the list
should be a dictionary with at least two keys. Write this list out to a file
using both YAML and JSON formats. The YAML file should be in the expanded form.
'''

import yaml
import json


def main():
    '''
    Write a Python program that creates a list. One of the elements of the list
    should be a dictionary with at least two keys. Write this list out to a file
    using both YAML and JSON formats. The YAML file should be in the expanded
    form.
    '''

    yaml_file = 'my_test.yml'
    json_file = 'my_test.json'

    my_dict = {
        'ip_addr': '172.31.200.1',
        'platform': 'cisco_ios',
        'vendor':   'cisco',
        'model':    '1921'
    }

    my_list = [
        'some string',
        99,
        18,
        my_dict,
        'another string',
        'final string'
    ]

    with open(yaml_file, "w") as f:
        f.write(yaml.dump(my_list, default_flow_style=False))

    with open(json_file, "w") as f:
        json.dump(my_list, f)


if __name__ == "__main__":
    main()
