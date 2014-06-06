#!/usr/bin/env python

'''

This is a solution to the below problem given the content we have
discussed in class.  It is not necessarily the best solution to the problem.
In other words, I generally only use things we have covered up to this point
in the class (with some exceptions which I will usually note). 

Python for Network Engineers
https://pynet.twb-tech.com
Learning Python


III. Write a new class, IPAddressWithNetmask, that is based upon
the IPAddress class created in exercise1 (i.e. use inheritance).
 The netmask should be stored in slash notation (i.e. /24).  With
this class you should be able to do the following:

>>> test_ip2 = IPAddressWithNetmask('172.31.255.1/24')
>>> test_ip2.ip_addr
'172.31.255.1'
>>> test_ip2.netmask
'/24'


If possible, the ip_addr attribute should be assigned via the
__init__ method in the IPAddress Class (in other words, call the
__init__ method of the base IPAddress class with '172.31.255.1' as
an argument).

All of the other methods from the IPAddress class should be left
unchanged.

    A. Create a new method in the IPAddressWithNetmask class that
converts the slash notation netmask to dotted decimal.

    B. You should be able to do the following when you are done:

>>> test_ip2 = IPAddressWithNetmask('172.31.255.1/24')
>>> test_ip2.ip_addr
'172.31.255.1'
>>> test_ip2.netmask
'/24'

>>> test_ip2.display_in_binary()
'10101100.00011111.11111111.00000001'
>>> test_ip2.display_in_hex()
'ac.1f.ff.01'
>>> test_ip2.is_valid()
True

>>> test_ip2.netmask_in_dotdecimal()
'255.255.255.0'

'''


from ex1_ip_addr_class import IPAddress


class IPAddressWithNetmask(IPAddress):
    '''
    Add a netmask to the IPAddress class
    '''

    def __init__(self, ip_addr):

        (ip_addr, netmask) = ip_addr.split("/")
        self.netmask = '/' + netmask

        # Call the base class
        IPAddress.__init__(self, ip_addr)


    def netmask_in_dotdecimal(self):
        '''
        Display the netmask in dotted decimal
        '''

        # Use the fact that you can repeat a string via multiplication
        netmask = int(self.netmask.strip("/"))
        one_string = '1' * netmask

        # Number of zeros
        zero_string = '0' * (32 - netmask)

        # New netmask string
        netmask_str = one_string + zero_string

        # Grab each octet
        octet1 = netmask_str[:8]
        octet2 = netmask_str[8:16]
        octet3 = netmask_str[16:24]
        octet4 = netmask_str[24:32]
        netmask_tmp = [octet1, octet2, octet3, octet4]

        # Convert from binary to decimal
        for i,octet in enumerate(netmask_tmp):
            # Must be a string to use the join method
            netmask_tmp[i] = str(int(octet,2))

        return '.'.join(netmask_tmp)


if __name__ == "__main__":

    # Some test code
    test_ip2 = IPAddressWithNetmask('172.31.255.1/24')

    print 
    print "%15s: %-40s" % ("IP", test_ip2.ip_addr)
    print "%15s: %-40s" % ("Netmask", test_ip2.netmask)
    print "%15s: %-40s" % ("Binary IP", test_ip2.display_in_binary()) 
    print "%15s: %-40s" % ("Hex IP", test_ip2.display_in_hex())
    print "%15s: %-40s" % ("IP Valid", test_ip2.is_valid())
    print "%15s: %-40s" % ("Netmask dot dec", test_ip2.netmask_in_dotdecimal() )
    print

    

