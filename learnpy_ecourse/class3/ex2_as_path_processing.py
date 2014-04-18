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


II. Modify the 'show ip bgp' exercise from class2.   Simplify the program using
the flow-control statements from this class.

>>>> 'show ip bgp' exercise from class2' (for reference) <<<<<

You have the following four lines from 'show ip bgp':

entry1 = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24      157.130.10.233         0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24     157.130.10.233        0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"

Note, in each case the AS_PATH starts with '701'.

Using split() and a list slice, how could you process each of these such that--
for each entry, you return an ip_prefix and the AS_PATH (the ip_prefix should be
a string; the AS_PATH should be a list):

Your output should look like this:

ip_prefix           as_path                                           
1.0.192.0/18        ['701', '38040', '9737']                          
1.1.1.0/24          ['701', '1299', '15169']                          
1.1.42.0/24         ['701', '9505', '17408', '2.1465']                
1.0.192.0/19        ['701', '6762', '6762', '6762', '6762', '38040', '9737']


Ideally, your logic should be the same for each entry (I say this because once I
teach you for loops, then I want to be able to process all of these in one four
loop).

If you can't figure this out using a list slice, you could also solve this using
pop().

>>>> 'show ip bgp' exercise from class2' (end) <<<<<

'''

entry1 = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24      157.130.10.233         0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24     157.130.10.233        0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"

print "\n%-20s %-50s" % ("ip_prefix", "as_path")

for entry in (entry1, entry2, entry3, entry4):
    entry_split = entry.split()
    ip_prefix = entry_split[1]
    as_path = entry_split[4:-1]
    print "%-20s %-50s" % (ip_prefix, as_path)

print "\n"
