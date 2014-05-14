#!/usr/bin/env python

'''

Disclaimer - This is a solution to the below problem given the content we have
discussed in class.  It is not necessarily the best solution to the problem.
In other words, I only use things we have covered up to this point in the class
(with some minor exceptions).

Python for Network Engineers
https://pynet.twb-tech.com
Learning Python

4. Create a function using your dotted decimal to binary conversion
code from Class3, exercise1.  In the function--do not prompt for
input and do not print to standard output.  The function should
take one variable 'ip_address' and should return the IP address in
dotted binary format always padded to eight binary digits (for
example, 00001010.01011000.00010001.00010111).  You might want to
create other functions as well (for example, the zero-padding to
eight binary digits).

'''


def pad_binary_digits(bin_octet):
    '''
    Pad the binary number to eight digits
    '''

    # prepend '0' to number until 8 chars long
    while True:
        if len(bin_octet) >= 8:
            break
        bin_octet = '0' + bin_octet

    return bin_octet


def convert_ip_to_binary(ip_address):
    '''
    Take an IP address in dotted-decimal format and convert it to a
    dotted-binary output (00001010.01011000.00010001.00010111).

    The binary digits should always be padded to eight digits

    return the new binary IP
    '''

    octets = ip_address.split(".")

    ip_addr_bin = []

    for octet in octets:

        # convert number to binary
        bin_octet = bin(int(octet))

        # strip off '0b' from front of string
        bin_octet = bin_octet[2:]

        # pad to 8 digits
        bin_octet = pad_binary_digits(bin_octet)

        # add octet to new list
        ip_addr_bin.append(bin_octet)


    # join binary number in dotted-binary format
    return ".".join(ip_addr_bin)



# Technique to allow importable and executable code to coexist (will explain in class#8)
if __name__ == '__main__':

    # Create a bunch of test cases
    test_ip_addresses = [ 
        '1.1.1.1',
        '223.255.255.255',
        '223.255.254.252',
        '223.248.240.224',
        '192.128.3.7',
        '223.0.0.0',
        '10.200.255.1',
        '192.168.17.1',  
    ]

    print

    # Run the test cases
    for ip in test_ip_addresses:

        binary_ip = convert_ip_to_binary(ip)
        print "%18s    %-40s" % (ip, binary_ip)

    print 

