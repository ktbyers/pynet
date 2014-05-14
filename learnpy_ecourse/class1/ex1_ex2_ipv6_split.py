#!/usr/bin/env python

'''

Disclaimer - This is a solution to the below problem given the content we have
discussed in class.  It is not necessarily the best solution to the problem.
In other words, I generally only use things we have covered up to this point
in the class (with some exceptions which I will usually note). 

Python for Network Engineers
https://pynet.twb-tech.com
Learning Python

1. Use the split method to divide the following IPv6 address into
groups of 4 hex digits (i.e. split on the ":")

FE80:0000:0000:0000:0101:A3EF:EE1E:1719

2. Use the join method to reunite your split IPv6 address back to
its original value.

'''

ipv6_addr = 'FE80:0000:0000:0000:0101:A3EF:EE1E:1719'

ipv6_sections = ipv6_addr.split(":")

print
print "IPv6 address split:"
print ipv6_sections
print

ipv6_new = ":".join(ipv6_sections)

print "IPv6 address re-joined:"
print ipv6_new
print

