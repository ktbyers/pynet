#!/usr/bin/env python

'''
This is a solution to the below problem given the content we have
discussed in class.  It is not necessarily the best solution to the problem.
In other words, I generally only use things we have covered up to this point
in the class (with some exceptions which I will usually note). 

Python for Network Engineers
https://pynet.twb-tech.com
Learning Python


I. Create a Python class representing an IPAddress.  The class
should have only one initialization variable--an IP address in
dotted decimal formation.  You should be able to do the following
with your class:

>>> test_ip = IPAddress('192.168.1.1')
>>> test_ip.ip_addr
'192.168.1.1'

    A. Write a method for this class that returns the IP address in
dotted binary format (each octet should be eight binary digits in
length).

>>> test_ip.display_in_binary()
'11000000.10101000.00000001.00000001'

    B. Write a method for this class that returns the IP address in
dotted hex format (each octet should be two hex digits in length).

>>> test_ip.display_in_hex()
'c0.a8.01.01'

    C. Using the IP address validation function from class8,
exercise1--create an is_valid() method that returns either True or
False depending on whether the IP address is valid.

>>> test_ip.is_valid()
True

'''


class IPAddress(object):
    '''
    A class representing an IP address
    '''
    
    def __init__(self, ip_addr):
        self.ip_addr = ip_addr


    def display_in_binary(self):
        '''
        Display the IP address in dotted binary format padded to eight 
        digits:

        11000000.10101000.00000001.00000001

        '''
        
        octets = self.ip_addr.split(".")

        binary_ip = []
        for octet in octets:
            # convert octet to binary
            octet_bin = bin(int(octet))
            (junk, octet_bin) = octet_bin.split('0b')

            # pad to 8 digits using rjust() method
            octet_bin = octet_bin.rjust(8, '0')
            binary_ip.append(octet_bin)

        return ".".join(binary_ip)


    def display_in_hex(self):
        '''
        Display the IP address in dotted hex format padded to eight 
        digits:

        c0.a8.01.01

        '''
   
        octets = self.ip_addr.split(".")

        hex_ip = [] 
        for octet in octets:
            # convert octet to hex
            octet_hex = hex(int(octet))
            (junk, octet_hex) = octet_hex.split('0x')
    
            # pad to 2 digits using rjust() method
            octet_hex = octet_hex.rjust(2, '0')
            hex_ip.append(octet_hex)

        return ".".join(hex_ip)


    def is_valid(self):
        '''
        Check if the IP address is valid
    
        Return either True or False
        '''
    
        valid_ip = True
    
        # Make sure IP has four octets
        octets = self.ip_addr.split('.')
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




if __name__ == "__main__":

    # Some simple testing
    test_ips = ['192.168.1.1', '0.255.1.1']

    for ip in test_ips:
        print "\nTesting IP: %s" % ip
        test_ip = IPAddress(ip)
        print "IP in binary: %s" % test_ip.display_in_binary() 
        print "IP in hex: %s" % test_ip.display_in_hex() 
        print "IP is valid: %s" % test_ip.is_valid()
        print

