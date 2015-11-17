#!/usr/bin/env python
from net_system.models import InventoryGroup
import argparse
import json
import django


def output_list_inventory(json_output):
    '''
    Output the --list data structure as JSON
    '''
    print json.dumps(json_output)

def find_host(search_host, inventory):
    '''
    Find the given variables for the given host and output them as JSON
    '''
    host_attribs = inventory.get(search_host, {})
    print json.dumps(host_attribs)

def ansible_local_init(ansible_inv):
    '''
    Initialize a Ansible 'local'
    '''
    ansible_inv['local'] = {}
    ansible_inv['local']['hosts'] = ['localhost']
    ansible_inv['local']['vars'] = {'ansible_connection': 'local'}

def ansible_group_init(ansible_inv, group_name):
    '''
    Initialize a new Ansible inventory group
    '''
    ansible_inv[group_name] = {}
    ansible_inv[group_name]['hosts'] = []
    ansible_inv[group_name]['vars'] = {}

def main():
    '''
    Ansible dynamic inventory experimentation
    Output dynamic inventory as JSON from statically defined data structures
    '''
    # Argument parsing
    parser = argparse.ArgumentParser(description="Ansible dynamic inventory")
    parser.add_argument("--list", help="Ansible inventory of all of the groups",
                        action="store_true", dest="list_inventory")
    parser.add_argument("--host", help="Ansible inventory of a particular host", action="store",
                        dest="ansible_host", type=str)

    cli_args = parser.parse_args()
    list_inventory = cli_args.list_inventory
    ansible_host = cli_args.ansible_host

    django.setup()

    ansible_inv = {}
    host_vars = {}
    ansible_local_init(ansible_inv)

    inventory_groups = InventoryGroup.objects.all()
    for a_group in inventory_groups:
        switches = a_group.networkswitch_set.all()

        # Configure group inventory
        ansible_group_init(ansible_inv, a_group.group_name)
        for a_switch in switches:
            ansible_inv[a_group.group_name]['hosts'].append(a_switch.device_name)
        ansible_inv[a_group.group_name]['vars']['ansible_connection'] = 'local'

        # Configure host inventory
        for a_switch in switches:
            host_vars[a_switch.device_name] = {}
            host_vars[a_switch.device_name]['device_type'] = a_switch.device_type
            host_vars[a_switch.device_name]['ip'] = a_switch.ip_address
            host_vars[a_switch.device_name]['management_ip'] = a_switch.management_ip
            host_vars[a_switch.device_name]['port'] = a_switch.port
            host_vars[a_switch.device_name]['username'] = a_switch.credentials.username
            host_vars[a_switch.device_name]['password'] = a_switch.credentials.password
            host_vars[a_switch.device_name]['switchports'] = []
            ports = a_switch.switchport_set.all()
            for a_port in ports:
                tmp_dict = {}
                tmp_dict[a_port.port_name] = {}
                tmp_dict[a_port.port_name]['mode'] = a_port.mode
                if a_port.mode == 'access':
                    tmp_dict[a_port.port_name]['access_vlan'] = a_port.access_vlan
                elif a_port.mode == 'trunk':
                    tmp_dict[a_port.port_name]['trunk_native_vlan'] = a_port.trunk_native_vlan
                    tmp_dict[a_port.port_name]['trunk_allowed_vlans'] = a_port.trunk_allowed_vlans
                tmp_dict[a_port.port_name]['lag_enabled'] = a_port.lag_enabled
                if a_port.lag_enabled:
                    tmp_dict[a_port.port_name]['lag_mode'] = a_port.lag_mode
                    tmp_dict[a_port.port_name]['lag_group'] = a_port.lag_group
                host_vars[a_switch.device_name]['switchports'].append(tmp_dict)


    if list_inventory:
        output_list_inventory(ansible_inv)

    if ansible_host:
        find_host(ansible_host, host_vars)

if __name__ == "__main__":
    main()
