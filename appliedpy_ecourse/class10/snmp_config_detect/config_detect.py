from snmp_helper import snmp_get_oid,snmp_get_oid_v3,snmp_extract


def snmp_wrapper(a_device, oid):
    '''
    snmp wrappers that extracts SNMP information from a_device object

    queries device by OID

    extracts snmp_data

    '''

    snmp_dict = snmp_preprocessor(a_device, oid)

    snmp_data = snmp_get_oid_v3(**snmp_dict)

    return snmp_extract(snmp_data)


def snmp_preprocessor(a_device, oid='.1.3.6.1.2.1.1.1.0'):
    '''
    Extract snmp parameters from NetworkDevice object

    Only supports SNMPv3
    '''

    if not a_device.snmp_credentials.snmp_mode == 'snmp3':
        raise ValueError("Invalid SNMP mode in config_detect {}".format(
            a_device.snmp_credentials.snmp_mode) )

    snmp_device = (
        a_device.ip_address,
        a_device.snmp_port
    )

    snmp_user = (
        a_device.snmp_credentials.username, 
        a_device.snmp_credentials.auth_key, 
        a_device.snmp_credentials.encrypt_key
    )

    auth_proto = a_device.snmp_credentials.auth_proto
    encrypt_proto = a_device.snmp_credentials.encrypt_proto

    return { 
        'snmp_device':  snmp_device,
        'snmp_user':    snmp_user,
        'oid':          oid,
        'auth_proto':   auth_proto,
        'encrypt_proto': encrypt_proto
    }
    
