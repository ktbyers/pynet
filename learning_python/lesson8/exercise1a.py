#!/usr/bin/env python
"""
Import the 'datetime' library. Print out the module that is being imported by datetime (the
__file__ attribute)

Import the Python ipaddress library. Print out the module that is being imported by ipaddress (the
__file__ attribte).

Import sys and use pprint to pretty print the sys.path.
"""
from __future__ import print_function, unicode_literals
import datetime
import ipaddress
import sys
from pprint import pprint


print()
print("datetime library imported from: ")
print(datetime.__file__)
print("\nipaddress library imported from: ")
print(ipaddress.__file__)
print("\nPython sys.path:")
pprint(sys.path)
print()
