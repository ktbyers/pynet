'''
Generate SwitchPort objects for database
'''
import django
from net_system.models import SwitchPort, NetworkSwitch


def create_access_port(network_switch, port_name, vlan):
    '''
    Create a SwitchPort object - access port
    '''
    debug = False
    new_port = SwitchPort.objects.get_or_create(
        port_name=port_name,
        mode='access',
        access_vlan=vlan,
        network_switch=network_switch
    )
    if debug:
        print new_port

def create_trunk_port(network_switch, port_name, native_vlan=1, allowed_vlans='all'):
    '''
    Create a SwitchPort object - trunk port
    '''
    debug = False
    new_port = SwitchPort.objects.get_or_create(
        port_name=port_name,
        mode='trunk',
        trunk_native_vlan=native_vlan,
        trunk_allowed_vlans=allowed_vlans,
        network_switch=network_switch
    )
    if debug:
        print new_port

def create_lag_port(network_switch, port_name, lag_mode='active',
                    lag_group=1, native_vlan=1, allowed_vlans='all'):
    '''
    Create a SwitchPort object - LAG
    '''
    debug = False
    new_port = SwitchPort.objects.get_or_create(
        port_name=port_name,
        mode='trunk',
        trunk_native_vlan=native_vlan,
        trunk_allowed_vlans=allowed_vlans,
        lag_enabled=True,
        lag_mode=lag_mode,
        lag_group=lag_group,
        network_switch=network_switch
    )
    if debug:
        print new_port

def main():
    '''
    Generate SwitchPort objects for database
    '''
    django.setup()
    switch1 = NetworkSwitch.objects.get(device_name='pynet-sw1')
    switch2 = NetworkSwitch.objects.get(device_name='pynet-sw2')
    switch3 = NetworkSwitch.objects.get(device_name='pynet-sw3')
    switch4 = NetworkSwitch.objects.get(device_name='pynet-sw4')

    print "Creating Switch1 port objects"
    # Standard access ports
    std_ports = [('Ethernet1', 1), ('Ethernet2', 100), ('Ethernet3', 200), ('Ethernet7', 200)]
    for switchport, vlan in std_ports:
        create_access_port(switch1, switchport, vlan)
    create_trunk_port(switch1, 'Ethernet4')
    create_lag_port(switch1, 'Ethernet5', lag_mode='active', lag_group=1)
    create_lag_port(switch1, 'Ethernet6', lag_mode='active', lag_group=1)
    create_trunk_port(switch1, 'Port-channel1')

    print "Creating Switch2 port objects"
    # Standard access ports
    std_ports = [('Ethernet1', 1), ('Ethernet2', 100), ('Ethernet3', 100),
                 ('Ethernet4', 200), ('Ethernet5', 300)]
    for switchport, vlan in std_ports:
        create_access_port(switch2, switchport, vlan)
    create_trunk_port(switch2, 'Ethernet6', native_vlan=300, allowed_vlans='100,200,300')
    create_trunk_port(switch2, 'Ethernet7', native_vlan=300, allowed_vlans='100,200,300')

    print "Creating Switch3 port objects"
    # Standard access ports
    std_ports = [('Ethernet1', 1), ('Ethernet2', 100), ('Ethernet3', 100), ('Ethernet4', 100),
                 ('Ethernet5', 100), ('Ethernet6', 200), ('Ethernet7', 200)]
    for switchport, vlan in std_ports:
        create_access_port(switch3, switchport, vlan)

    print "Creating Switch4 port objects"
    # Standard access ports
    std_ports = [('Ethernet1', 1), ('Ethernet2', 100), ('Ethernet3', 100),
                 ('Ethernet4', 100), ('Ethernet5', 100)]
    for switchport, vlan in std_ports:
        create_access_port(switch4, switchport, vlan)
    create_trunk_port(switch4, 'Ethernet6', native_vlan=300, allowed_vlans='100,200,300')
    create_trunk_port(switch4, 'Ethernet7', native_vlan=300, allowed_vlans='100,200,300')

if __name__ == "__main__":
    main()
