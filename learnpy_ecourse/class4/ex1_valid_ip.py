#!/usr/bin/env python

'''

Disclaimer - This is a solution to the below problem given the content we have
discussed in class.  It is not necessarily the best solution to the problem.
In other words, I generally only use things we have covered up to this point
in the class (with some exceptions which I will usually note). 

Python for Network Engineers
https://pynet.twb-tech.com
Learning Python

Prompt a user to input an IP address.  Re-using some of the code from class3,
exercise4--determine if the IP address is valid.  Continue prompting the user
to re-input an IP address until a valid IP address is input.

'''

not_done = True
while not_done:

    ip_addr = raw_input("\n\nPlease enter an IP address: ")

    # Check for valid ip address--would be much nice to be a function :-)

    # This checking code is based upon the code from class3, exercise#4
    # https://github.com/ktbyers/pynet/blob/master/learnpy_ecourse/class3/ex4_ip_address_valid.py

    valid_ip = True
    
    # Make sure IP has four octets
    octets = ip_addr.split('.')
    if len(octets) != 4:
        print "\nOoops, you don't have 4 octets - try again."
        continue
    
    # convert octet from string to int
    for i,octet in enumerate(octets):
    
        try:
            octets[i] = int(octet)
        except ValueError:
            # couldn't convert octet to an integer
            valid_ip = False

    # Go to next iteration of while loop if I don't have 4 integers
    if not valid_ip:    
        print "\nYou entered an octet that wasn't an integer (or a blank", \
              "octet) - that's not going to work."
        continue

    # map variables to elements of octets list
    first_octet, second_octet, third_octet, fourth_octet = octets
    
    # Check first_octet meets conditions
    if first_octet < 1:
        valid_ip = False
    elif first_octet > 223:
        valid_ip = False
    elif first_octet == 127:
        valid_ip = False
    
    # Check 169.254.X.X condition
    if first_octet == 169 and second_octet == 254:
        valid_ip = False
    
    # Check 2nd - 4th octets
    for octet in (second_octet, third_octet, fourth_octet):
        if (octet < 0) or (octet > 255):
            valid_ip = False
    
    
    if valid_ip:
        not_done = False
    else:
        print "\nWell, you screwed-up something on that IP address - do it again please."
   
 
print "\n\nThe IP address is valid: %s\n" % ip_addr
