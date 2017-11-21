#!/usr/bin/env python
"""
Create three variables: ip_addr1, ip_addr2, ip_addr3 representing three IP addresses.

print these three variables to standard output using a single print statement.

Make your print statement compatible with both Python2 and Python2 (i.e. you should be able
to run this same program using either PY2 or PY3).

If you are using Linux or MacOS make your program executable by adding a shebang line and
by changing the files permissions (i.e. chmod 755 <file_name.py>)
"""
from __future__ import print_function

ip_addr1 = '192.168.16.1'
ip_addr2 = '10.10.1.1'
ip_addr3 = '172.16.31.17'

print(ip_addr1, ip_addr2, ip_addr3)
