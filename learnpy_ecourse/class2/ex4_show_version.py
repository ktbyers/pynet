#!/usr/bin/env python

'''

Disclaimer - This is a solution to the below problem given the content we have
discussed in class.  It is not necessarily the best solution to the problem.
In other words, I only use things we have covered up to this point in the class.

Python for Network Engineers
https://pynet.twb-tech.com
Learning Python
Class#2

4. You have the following string from "show version" on a Cisco router:

cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version
15.0(1)M4, RELEASE SOFTWARE (fc1)"

Note, the string is a single line; there is no newline in the string.

How would you process this string to retrieve only the IOS version?


ios_version = "15.0(1)M4"

Try to make it generic (i.e. assume that the IOS version can change).  

You can assume that the commas divide this string into four sections and that
the string will always have 'Cisco IOS Software', 'Version', and 'RELEASE
SOFTWARE' in it.

'''

cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), \
Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"
ios_version = cisco_ios.split(",")[2]
ios_version = ios_version.split("Version ")[1]
print ios_version
