'''
Create an SnmpCredentials object using the SNMPv3 credentials of username = 
'pysnmp' and auth_key/encrypt_key = '*********'.

Update the two Cisco NetworkDevice objects such that they reference this 
SnmpCredentials object.
'''

from net_system.models import NetworkDevice,SnmpCredentials
import django

if __name__ == "__main__":

    django.setup()

    # Create SnmpCredentials object (if it doesn't exist)
    (cisco_snmp_creds, created) = SnmpCredentials.objects.get_or_create(
        snmp_mode = 'snmp3',
        description = 'standard cisco snmpv3 credentials',
        username = 'pysnmp',
        auth_proto = 'sha',
        auth_key = '*********',
        encrypt_proto = 'aes128',
        encrypt_key = '*********',
    )

    # Obtain all of the network devices
    net_devices = NetworkDevice.objects.all()
   
    # Set snmp_port, snmp_credentials for network device
    for a_device in net_devices:
        if 'cisco' in a_device.device_class:
            if a_device.device_name == 'pynet-rtr1':
                a_device.snmp_port = 7961
            elif a_device.device_name == 'pynet-rtr2':
                a_device.snmp_port = 8061

            a_device.snmp_credentials = cisco_snmp_creds
            a_device.save()

    # Verify cisco devices have correct port and snmp credentials
    for a_device in net_devices:
        if 'cisco' in a_device.device_class:
            print a_device, a_device.snmp_port, a_device.snmp_credentials
