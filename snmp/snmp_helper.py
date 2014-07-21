'''
Requires the pysnmp version4 library

Example usage:

>>> from snmp_helper import snmp_get_oid,snmp_extract
>>> 
>>> COMMUNITY_STRING = '<COMMUNITY>'
>>> SNMP_PORT = 161
>>> a_device = ('1.1.1.1', COMMUNITY_STRING, SNMP_PORT)

Use the MIB-2 sysDescr as a test
>>> snmp_data = snmp_get_oid(a_device, oid='.1.3.6.1.2.1.1.1.0', display_errors=True)
>>> snmp_data

[(MibVariable(ObjectName(1.3.6.1.2.1.1.1.0)), DisplayString(hexValue='436973636f
20494f5320536f6674776172652c204338383020536f667477617265202843383830444154412d55
4e4956455253414c4b392d4d292c2056657273696f6e2031352e302831294d342c2052454c454153
4520534f4654574152452028666331290d0a546563686e6963616c20537570706f72743a20687474
703a2f2f7777772e636973636f2e636f6d2f74656368737570706f72740d0a436f70797269676874
2028632920313938362d3230313020627920436973636f2053797374656d732c20496e632e0d0a43
6f6d70696c6564204672692032392d4f63742d31302030303a30322062792070726f645f72656c5f
7465616d'))]

>>> output = snmp_extract(snmp_data)
>>> print output
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team

'''

from pysnmp.entity.rfc3413.oneliner import cmdgen


def snmp_get_oid(a_device, oid='.1.3.6.1.2.1.1.1.0', display_errors=False):
    '''
    Retrieve the given OID

    Default OID is MIB2, sysDescr

    a_device is a tuple = (a_host, community_string, snmp_port)
    '''

    a_host, community_string, snmp_port = a_device
    snmp_target = (a_host, snmp_port)

    # Create a PYSNMP cmdgen object
    cmd_gen = cmdgen.CommandGenerator()

    (error_detected, error_status, error_index, snmp_data) = cmd_gen.getCmd(
        cmdgen.CommunityData(community_string),
        cmdgen.UdpTransportTarget(snmp_target),
        oid,
        lookupNames=True, lookupValues=True
    )

    if not error_detected:
        return snmp_data
    else:
        if display_errors:
            print 'ERROR DETECTED: '
            print '    %-16s %-60s' % ('error_message', error_detected)
            print '    %-16s %-60s' % ('error_status', error_status)
            print '    %-16s %-60s' % ('error_index', error_index)
        return None


def snmp_extract(snmp_data):
    '''
    Unwrap the SNMP response data and return in a readable format

    Assumes only a single list element is returned
    '''

    if len(snmp_data) > 1:
        raise ValueError("snmp_extract only allows a single element")

    if len(snmp_data) == 0:
        return None
    else:
        # Unwrap the data which is returned as a tuple wrapped in a list
        return snmp_data[0][1].prettyPrint()
