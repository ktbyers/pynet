from net_system.models import NetworkSwitch, InventoryGroup
from net_system.models import Credentials
from getpass import getpass

import django

def main():
    django.setup()

    management_ip = raw_input("Please enter IP address: ")
    my_switches = (('pynet-sw1', 8222, '10.220.88.28'),
                   ('pynet-sw2', 8322, '10.220.88.29'),
                   ('pynet-sw3', 8422, '10.220.88.30'),
                   ('pynet-sw4', 8522, '10.220.88.31'))

    passwd = getpass()

    # Create Arista inventory group
    arista_group = InventoryGroup.objects.get_or_create(group_name='arista')
    print arista_group

    # Create credential object
    arista_creds = Credentials.objects.get_or_create(
        username='admin1',
        password=passwd,
        description='Arista credentials'
    )
    print arista_creds

    # Create four switch objects
    for switch_name, ssh_port, ip_addr in my_switches:
        switch_obj = NetworkSwitch.objects.get_or_create(
            device_name=switch_name,
            device_type='arista_eos',
            ip_address=ip_addr,
            management_ip=management_ip,
            port=ssh_port,
            group_name=arista_group[0],
            credentials = arista_creds[0],
        )
        print switch_obj

if __name__ == "__main__":
    main()
