#!/usr/bin/env python
"""Read in the "show_ip_int_brief.txt" file into your program using the
.readlines() method.

Obtain the list entry associated with the FastEthernet4 interface. You can
just hard-code the index at this point since we haven't covered for-loops
or regular expressions:

Use the string .split() method to obtain both the IP address and the
corresponding interface associated with the IP.

Create a two element tuple from the result (intf_name, ip_address).

Print that tuple to the screen.

Use pycodestyle on this script. Get the warnings/errors to zero. You might need
to 'pip install pycodestyle' on your computer (should be able to type this from
the shell prompt). Alternatively, you can type:

  'python -m pip install pycodestyle'.

"""
from __future__ import print_function, unicode_literals

with open("show_ip_int_brief.txt") as f:
    show_ip_int_brief = f.readlines()

fa4_ip = show_ip_int_brief[5].strip()
fields = fa4_ip.split()
intf = fields[0]
ip_address = fields[1]

my_results = (intf, ip_address)
print(my_results)
