#!/usr/bin/env python

'''

Disclaimer - This is a solution to the below problem given the content we have
discussed in class.  It is not necessarily the best solution to the problem.
In other words, I generally only use things we have covered up to this point
in the class (with some exceptions which I will usually note). 

Python for Network Engineers
https://pynet.twb-tech.com
Learning Python


Parse the below 'show version' data and obtain the following items (vendor, 
model, os_version, uptime, and serial_number).  Try to make your string parsing
generic i.e. it would work for other Cisco IOS devices. 

The following are reasonable strings to look for:
'Cisco IOS Software' for vendor and os_version
'bytes of memory' for model
'Processor board ID' for serial_number
' uptime is ' for uptime

Store these variables (vendor, model, os_version, uptime, and serial_number) in 
a dictionary.  Print the dictionary to standard output when done.

Note, "Cisco IOS Software...Version 15.0(1)M4...(fc1)" is one line.

'''

import pprint


show_version = '''
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)

Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
ROM: System Bootstrap, Version 12.4(22r)YB5, RELEASE SOFTWARE (fc1)

twb-sf-881 uptime is 7 weeks, 5 days, 19 hours, 23 minutes
System returned to ROM by reload at 15:33:36 PST Fri Feb 28 2014
System restarted at 15:34:09 PST Fri Feb 28 2014

System image file is "flash:c880data-universalk9-mz.150-1.M4.bin"
Last reload type: Normal Reload
Last reload reason: Reload Command

Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.

Processor board ID FTX1000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)

License Info:
License UDI:
-------------------------------------------------
Device#   PID                   SN
-------------------------------------------------
*0        CISCO881-SEC-K9       FTX1000038X

License Information for 'c880-data'
    License Level: advipservices   Type: Permanent
    Next reboot license Level: advipservices

Configuration register is 0x2102

'''

# Convert the show version to a list - one entry per line
show_ver_list = show_version.split("\n")

router_dict = {}

# Iterate over the show version data
for line in show_ver_list:

    # Vendor and OS Version processing
    if 'Cisco IOS Software' in line:
        router_dict['vendor'] = 'Cisco'
        os_version = line.split(',')[2]
        router_dict['os_version'] = os_version.split('Version ')[1]
       
    # Model processing (note, 'Cisco 881...bytes of memory' is on one line)
    if 'bytes of memory' in line:
        # The model will be the second word in this line
        router_dict['model'] = line.split()[1] 

    # Serial number processing
    if 'Processor board ID' in line:
        router_dict['serial_number'] = line.split('Processor board ID ')[1]

    # Uptime processing
    if ' uptime is ' in line:
        uptime = line.split(' uptime is ')[1]
        uptime = uptime.strip()
        router_dict['uptime'] = uptime



# Print dictionary to standard output
print 
pprint.pprint(router_dict)
print 
