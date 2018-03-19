#!/usr/bin/env python
"""
Write a python program where you store a device in an external Python module as a dictionary.
Pass that device into Netmiko and connect to the device successfully and print out the device's
prompt.

Repeat this, but with three device's

"""
from __future__ import print_function, unicode_literals
import datetime
import ipaddress
import sys
from pprint import pprint


print()
print(datetime.__file__)
print(ipaddress.__file__)
pprint(sys.path)
print()
