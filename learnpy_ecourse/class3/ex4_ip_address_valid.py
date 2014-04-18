#!/usr/bin/env python

'''

Disclaimer - This is a solution to the below problem given the content we have
discussed in class.  It is not necessarily the best solution to the problem.
In other words, I only use things we have covered up to this point in the class.
Well, with some exceptions (I use try / except below).

Python for Network Engineers
https://pynet.twb-tech.com
Learning Python
Class#3


V. Create a script that checks the validity of an IP address.  The IP address
should be supplied on the command line.
    A. Check that the IP address contains 4 octets.
    B. The first octet must be between 1 - 223.
    C. The first octet cannot be 127.
    D. The IP address cannot be in the 169.254.X.X address space.
    E. The last three octets must range between 0 - 255.

    For output, print the IP and whether it is valid or not.

'''

import sys

if len(sys.argv) != 2:
    # Exit the script
    sys.exit("Usage: ./ex4_ip_address_valid.py <ip_address>")

ip_addr = sys.argv.pop()

valid_ip = True

# Make sure IP has four octets
octets = ip_addr.split('.')
if len(octets) != 4:
    sys.exit("\n\nInvalid IP address: %s\n" % ip_addr)

# convert octet from string to int
for i,octet in enumerate(octets):

    # I haven't told you about exception handling yet (soon)
    # You could do without this, the script will just crash
    # on certain invalid input (for example, '1.1.1.')
    try:
        octets[i] = int(octet)
    except ValueError:
        # couldn't convert octet to an integer
        sys.exit("\n\nInvalid IP address: %s\n" % ip_addr)


# map variables to elements of octets list
first_octet, second_octet, third_octet, fourth_octet = octets

# Check first_octet meets conditions
if first_octet < 1:
    valid_ip = False
elif first_octet > 223:
    valid_ip = False
elif first_octet == 127:
    valid_ip = False

# Check 169.254.X.X condition
if first_octet == 169 and second_octet == 254:
    valid_ip = False

# Check 2nd - 4th octets
for octet in (second_octet, third_octet, fourth_octet):
    if (octet < 0) or (octet > 255):
        valid_ip = False


if valid_ip:
    print "\n\nThe IP address is valid: %s\n" % ip_addr
else:
    sys.exit("\n\nInvalid IP address: %s\n" % ip_addr)



