#!/usr/bin/env python

'''

Disclaimer - This is a solution to the below problem given the content we have
discussed in class.  It is not necessarily the best solution to the problem.
In other words, I generally only use things we have covered up to this point
in the class (with some exceptions which I will usually note). 

Python for Network Engineers
https://pynet.twb-tech.com
Learning Python

3. In the test3.py (from class email week1), how would you modify the script to
remove the trailing newline on the end of 192.168.1.1?

'''

import fileinput

for line in fileinput.input():
    line = line.strip()
    print line.split(".")

