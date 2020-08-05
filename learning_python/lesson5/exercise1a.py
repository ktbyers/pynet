#!/usr/bin/env python
"""
Create an ssh_conn function. This function should have three parameters: ip_addr, username, and
password. The function should print out each of these three variables and clearly indicate which
variable it is printing out.

Call this ssh_conn function using entirely positional arguments.

Call this ssh_conn function using entirely named arguments.

Call this ssh_conn function using a mix of positional and named arguments.
"""
from __future__ import print_function, unicode_literals


def ssh_conn(ip_addr, username, password):
    print("-" * 80)
    print("IP Addr: {}".format(ip_addr))
    print("Username: {}".format(username))
    print("Password: {}".format(password))
    print("-" * 80)


# Positional args
ssh_conn("192.168.1.1", "admin", "cisco123")

# Named args
ssh_conn(ip_addr="192.168.1.1", username="admin", password="cisco123")

# Mixing named and positional args
ssh_conn("192.168.1.1", password="cisco123", username="admin1")
