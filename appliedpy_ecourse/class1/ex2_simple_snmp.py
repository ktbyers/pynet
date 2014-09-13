'''
Applied Python Course, Class1, Exercise 2c

Note, you will need to update the IP and COMMUNITY_STRING to use this script.

'''

import snmp_helper
 
COMMUNITY_STRING = '*******'
IP = '10.10.10.10'

pynet_rtr1 = (IP, COMMUNITY_STRING, 7961)
pynet_rtr2 = (IP, COMMUNITY_STRING, 8061)

sys_descr = '1.3.6.1.2.1.1.1.0'
sys_name = '1.3.6.1.2.1.1.5.0'


for a_device in (pynet_rtr1, pynet_rtr2):

    print "\n*********************"
    for the_oid in (sys_name, sys_descr):
        snmp_data = snmp_helper.snmp_get_oid(a_device, oid=the_oid) 
        output = snmp_helper.snmp_extract(snmp_data)

        print output
    print "*********************"

print
