#!/usr/bin/env python

'''

Disclaimer - This is a solution to the below problem given the content we have
discussed in class.  It is not necessarily the best solution to the problem.
In other words, I generally only use things we have covered up to this point
in the class (with some exceptions which I will usually note). 

Python for Network Engineers
https://pynet.twb-tech.com
Learning Python

5. Write a program that prompts a user for an IP address, then
checks if the IP address is valid, and then converts the IP address
to binary (dotted decimal format).  Re-use the functions created in
exercises 3 and 4 ('import' the functions into your new program).

'''

from ex3_valid_ip import valid_ip
from ex4_binary_converter import convert_ip_to_binary

ip_addr = raw_input("\n\nPlease enter an IP address: ")

if valid_ip(ip_addr):
    print "\n%18s    %-40s\n" % (ip_addr, convert_ip_to_binary(ip_addr))
else:
    print "\nYou entered an invalid IP address!\n"
    
