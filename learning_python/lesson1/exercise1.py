#!/usr/bin/env python
"""Create a Python script that has three variables: ip_addr1, ip_addr2, ip_addr3 (representing
three corresponding IP addresses). Print these three variables to standard output using a single
print statement.

Make your print statement compatible with both Python2 and Python3.

If you are using either Linux or MacOS make your program executable by adding a shebang line and
by changing the files permissions (i.e. chmod 755 exercise1.py).
"""
from __future__ import print_function

ip_addr1 = '192.168.16.1'
ip_addr2 = '10.10.1.1'
ip_addr3 = '172.16.31.17'

print(ip_addr1, ip_addr2, ip_addr3)
