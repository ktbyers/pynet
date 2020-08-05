#!/usr/bin/env python
"""
Read the 'show_lldp_neighbors_detail.txt' file. Loop over the lines of this file. Keep reading the
lines until you have encountered the remote "System Name" and remote "Port id". Save these two items
into variables and print them to the screen. You should extract only the system name and port id
from the lines (i.e. your variables should only have 'twb-sf-hpsw1' and '15'). Break out of your
loop once you have retrieved these two items.
"""
from __future__ import unicode_literals, print_function


with open("show_lldp_neighbors_detail.txt") as f:
    show_lldp = f.read()

system_name, port_id = (None, None)
for line in show_lldp.splitlines():
    if "System Name: " in line:
        _, system_name = line.split("System Name: ")
    elif "Port id: " in line:
        _, port_id = line.split("Port id: ")

    if port_id and system_name:
        break

print()
print("System Name: {}".format(system_name))
print("Port ID: {}".format(port_id))
print()
