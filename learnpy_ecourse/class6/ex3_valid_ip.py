#!/usr/bin/env python

'''

Disclaimer - This is a solution to the below problem given the content we have
discussed in class.  It is not necessarily the best solution to the problem.
In other words, I generally only use things we have covered up to this point
in the class (with some exceptions which I will usually note). 

Python for Network Engineers
https://pynet.twb-tech.com
Learning Python

3a. Convert the IP address validation code (Class4, exercise1) into
a function, take one variable 'ip_address' and return either True
or False (depending on whether 'ip_address' is a valid IP).  Only
include IP address checking in the function--no prompting for
input, no printing to standard output.


3b. Import this IP address validation function into the Python
interpreter shell and test it (use both 'import x' and 'from x
import y').

Here is some brief testing of this function in the Python shell:

>>> import ex3_valid_ip
>>> ex3_valid_ip.valid_ip('1.1.1.1')
True
>>> ex3_valid_ip.valid_ip('0.1.1.1')
False
>>> 
>>> 
>>> from ex3_valid_ip import valid_ip
>>> valid_ip('223.17.19.1')
True
>>> valid_ip('223.17.19.256')
False
>>> 

'''

def valid_ip(ip_address):
    '''
    Check if the IP address is valid

    Return either True or False
    '''

    valid_ip = True

    # Make sure IP has four octets
    octets = ip_address.split('.')
    if len(octets) != 4:
        return False
    
    # convert octet from string to int
    for i,octet in enumerate(octets):
    
        try:
            octets[i] = int(octet)
        except ValueError:
            # couldn't convert octet to an integer
            return False
    
    
    # map variables to elements of octets list
    first_octet, second_octet, third_octet, fourth_octet = octets
    
    # Check first_octet meets conditions
    if first_octet < 1:
        return False
    elif first_octet > 223:
        return False
    elif first_octet == 127:
        return False
    
    # Check 169.254.X.X condition
    if first_octet == 169 and second_octet == 254:
        return False
    
    # Check 2nd - 4th octets
    for octet in (second_octet, third_octet, fourth_octet):
        if (octet < 0) or (octet > 255):
            return False
  
 
    # Passed all of the checks
    return True 
   


# Technique to allow importable and executable code to coexist (will explain in class#8)
if __name__ == '__main__':

    # Create a bunch of test cases
    test_ip_addresses = {
        '192.168.1'     :   False,
        '10.1.1.'       :   False,
        '10.1.1.x'      :   False,
        '0.77.22.19'    :   False,
        '-1.88.99.17'   :   False,
        '241.17.17.9'   :   False,
        '127.0.0.1'     :   False,
        '169.254.1.9'   :   False,
        '192.256.7.7'   :   False,
        '192.168.-1.7'  :   False,
        '10.1.1.256'    :   False,
        '1.1.1.1'       :   True,
        '223.255.255.255':  True,
        '223.0.0.0'     :   True,
        '10.200.255.1'  :   True,
        '192.168.17.1'  :   True,
    }

    print

    # Run the test cases
    for ip,expected_return in test_ip_addresses.items():

        func_test = valid_ip(ip)

        # Make the output format nicer
        dots_to_print = (25 - len(ip)) * '.'

        if func_test == expected_return:
            print "Testing %s %s %s" % (ip, dots_to_print, 'ok')
        else:
            print "Testing %s %s %s" % (ip, dots,to_print, 'failed')

    print 
