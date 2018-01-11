#!/usr/bin/env python
"""
Read in the "show_arp.txt" file using the readlines() method. Use a list slice to
remove the header line.

Use pretty print to print out the resulting list to the screen:
----
from pprint import pprint
pprint(some_var)
----

Use the list .sort() method to sort the list based on IP address.

Create a new list slice that is only the first three ARP entries. Print this to the screen.
"""
from __future__ import print_function, unicode_literals
from pprint import pprint

with open("show_arp.txt") as f:
    show_arp = f.readlines()

show_arp = show_arp[1:]
pprint(show_arp)

show_arp.sort()
pprint(show_arp[:3])
