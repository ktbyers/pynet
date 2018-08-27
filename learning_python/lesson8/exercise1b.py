#!/usr/bin/env python
"""
In a separate Python file named 'my_devices.py' define a dictionary named 'rtr1' with the following
key-value pairs:

host = rtr1.domain.com
username = cisco
password = cisco123
device_type = cisco_ios

Import my_devices into this program and print the rtr1 dictionary to the screen using pprint
"""
from __future__ import print_function, unicode_literals
from pprint import pprint
import my_devices


print()
pprint(my_devices.rtr1)
print()
