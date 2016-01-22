'''
Requires the pysnmp4 library

Example usage (SNMPv1/SNMPv2c):

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


Example usage (SNMPv3):

>>> from snmp_helper import snmp_get_oid_v3,snmp_extract
>>>
>>> snmp_device = ('10.10.10.10', 161)

>>> a_user = <snmpv3_user>
>>> auth_key = <snmpv3_auth_key>
>>> encrypt_key = <snmpv3_encrypt_key>
>>> snmp_user = (a_user, auth_key, encrypt_key)

OID to query
>>> sys_descr = '1.3.6.1.2.1.1.1.0'

Defaults to using AES128 and SHA1
>>> snmp_data = snmp_get_oid_v3(snmp_device, snmp_user, oid=sys_descr)
>>> output = snmp_extract(snmp_data)

>>> print output
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.4(2)T1, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2014 by Cisco Systems, Inc.
Compiled Thu 26-Jun-14 14:15 by prod_rel_team

'''

from __future__ import print_function
from pysnmp.entity.rfc3413.oneliner import cmdgen


def snmp_get_oid_v3(snmp_device, snmp_user, oid='.1.3.6.1.2.1.1.1.0', auth_proto='sha',
                    encrypt_proto='aes128', display_errors=True):
    '''
    Retrieve the given OID

    Default OID is MIB2, sysDescr

    snmp_device is a tuple = (hostname_or_IP, snmp_port)
    snmp_user is a tuple = (user_name, auth_key, encrypt_key)

    Defaults to SHA1-AES128 for authentication + encryption

    auth_proto can be 'sha' or 'md5' or 'none'
    encrypt_proto can be 'aes128', 'aes192', 'aes256', '3des', 'des', or 'none'


    From PySNMP manuals:  http://pysnmp.sourceforge.net/docs/current/security-configuration.html

    Optional authProtocol parameter may be used to specify non-default hash function algorithm.
    Possible values include:
    usmHMACMD5AuthProtocol -- MD5-based authentication protocol
    usmHMACSHAAuthProtocol -- SHA-based authentication protocol
    usmNoAuthProtocol -- no authentication to use (default)

    Optional privProtocol parameter may be used to specify non-default ciphering algorithm.
    Possible values include:
    usmDESPrivProtocol -- DES-based encryption protocol
    usmAesCfb128Protocol -- AES128-based encryption protocol (RFC3826)
    usm3DESEDEPrivProtocol -- triple DES-based encryption protocol (Extended Security Options)
    usmAesCfb192Protocol -- AES192-based encryption protocol (Extended Security Options)
    usmAesCfb256Protocol -- AES256-based encryption protocol (Extended Security Options)
    usmNoPrivProtocol -- no encryption to use (default)

    '''

    # unpack snmp_user
    a_user, auth_key, encrypt_key = snmp_user

    auth_proto_map = {
        'sha':  cmdgen.usmHMACSHAAuthProtocol,
        'md5':  cmdgen.usmHMACMD5AuthProtocol,
        'none': cmdgen.usmNoAuthProtocol
    }

    if auth_proto in auth_proto_map.keys():
        auth_protocol = auth_proto_map[auth_proto]
    else:
        raise ValueError("Invalid authentication protocol specified: %s" % auth_proto)

    encrypt_proto_map = {
        'des':      cmdgen.usmDESPrivProtocol,
        '3des':     cmdgen.usm3DESEDEPrivProtocol,
        'aes128':   cmdgen.usmAesCfb128Protocol,
        'aes192':   cmdgen.usmAesCfb192Protocol,
        'aes256':   cmdgen.usmAesCfb256Protocol,
        'none':     cmdgen.usmNoPrivProtocol,
    }

    if encrypt_proto in encrypt_proto_map.keys():
        encrypt_protocol = encrypt_proto_map[encrypt_proto]
    else:
        raise ValueError("Invalid encryption protocol specified: %s" % encrypt_proto)


    # Create a PYSNMP cmdgen object
    cmd_gen = cmdgen.CommandGenerator()

    (error_detected, error_status, error_index, snmp_data) = cmd_gen.getCmd(

        cmdgen.UsmUserData(a_user, auth_key, encrypt_key,
                           authProtocol=auth_protocol,
                           privProtocol=encrypt_protocol, ),
        cmdgen.UdpTransportTarget(snmp_device),
        oid,
        lookupNames=True, lookupValues=True
    )

    if not error_detected:
        return snmp_data
    else:
        if display_errors:
            print('ERROR DETECTED: ')
            print('    %-16s %-60s' % ('error_message', error_detected))
            print('    %-16s %-60s' % ('error_status', error_status))
            print('    %-16s %-60s' % ('error_index', error_index))
        return None


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
            print('ERROR DETECTED: ')
            print('    %-16s %-60s' % ('error_message', error_detected))
            print('    %-16s %-60s' % ('error_status', error_status))
            print('    %-16s %-60s' % ('error_index', error_index))
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
