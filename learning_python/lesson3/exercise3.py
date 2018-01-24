#!/usr/bin/env python
'''
Read in the 'show_lldp_neighbors_detail.txt' file. Use a while loop to keep reading the file
contents until you have encountered the remote "system Name" and remote "Port id". After you
have both of those break out of the while loop and save the two items into the system_name and
port_id variables.
'''


with open("show_lldp_neighbors_detail.txt") as f:
    show_lldp = f.readlines()

system_name, port_id = (None, None)
while True:
    line = show_lldp.pop(0)
    line = line.strip()
    if 'System Name: ' in line:
        _, system_name = line.split('System Name: ')
    elif 'Port id: ' in line:
        _, port_id = line.split('Port id: ')

    if port_id and system_name:
        break

print()
print("System Name: {}".format(system_name))
print("Port ID: {}".format(port_id))
print()
