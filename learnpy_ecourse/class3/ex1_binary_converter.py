#!/usr/bin/env python

'''

Disclaimer - This is a solution to the below problem given the content we have
discussed in class.  It is not necessarily the best solution to the problem.
In other words, I only use things we have covered up to this point in the class
(with some minor exceptions).

Python for Network Engineers
https://pynet.twb-tech.com
Learning Python
Class#3

I. Create an IP address converter (dotted decimal to binary).  This will be 
similar to what we did in class2 except:

    A. Make the IP address a command-line argument instead of prompting the user
for it.
            ./binary_converter.py 10.88.17.23

    B. Simplify the script logic by using the flow-control statements that we 
learned in this class.

    C. Zero-pad the digits such that the binary output is always 8-binary digits
long.  Strip off the leading '0b' characters.  For example,

        OLD:     0b1010
        NEW:    00001010

    D. Print to standard output using a dotted binary format.  For example,

        IP address          Binary
        10.88.17.23        00001010.01011000.00010001.00010111

    Note, you will probably need to use a 'while' loop and a 'break' statement 
for part C.

        while True:
            ...
            break       # on some condition (exit the while loop)

    Python will execute this loop again and again until the 'break' is encountered. 

'''

import sys

if len(sys.argv) != 2:
    # Exit the script
    sys.exit("Usage: ./ex1_binary_converter.py <ip_address>")


ip_addr = sys.argv.pop()
octets = ip_addr.split(".")

# create a blank list (needed because I use .append() method below)
ip_addr_bin = []

if len(octets) == 4:

    for octet in octets:

        bin_octet = bin(int(octet))

        # strip off '0b' from front of string (you can slice a string also)
        bin_octet = bin_octet[2:]

        # prepend '0' to number until 8 chars long
        while True:
            if len(bin_octet) >= 8:
                break
            bin_octet = '0' + bin_octet

        # add octet to new list
        ip_addr_bin.append(bin_octet)


    # join binary number in dotted-binary format
    ip_addr_bin = ".".join(ip_addr_bin)

    # print the output
    print "\n%-15s %-45s" % ("IP address", "Binary")
    print "%-15s %-45s\n\n" % (ip_addr, ip_addr_bin)

else:
    sys.exit("Invalid IP address entered")


