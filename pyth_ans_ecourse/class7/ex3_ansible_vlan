#!/usr/bin/env python
'''
Challenge exercise (optional) -- Using Arista's eAPI, write an Ansible module
that adds a VLAN (both a VLAN ID and a VLAN name).  Do this in an idempotent
manner i.e. only add the VLAN if it doesn't exist; only change the VLAN name
if it is not correct.

To simplify this process, use the .eapi.conf file to store the connection
arguments (username, password, host, port, transport).
'''

import pyeapi

# Reuse functions from class5, exercise2
from eapi_vlan import check_vlan_exists, configure_vlan
from ansible.module_utils.basic import *

def main():
    '''
    Simple Ansible module to create an Arista VLAN
    '''
    module = AnsibleModule(
        argument_spec=dict(
            arista_sw=dict(required=True),
            vlan_id=dict(required=True),
            vlan_name=dict(required=False),
        )
    )

    vlan_id = module.params['vlan_id']
    vlan_name = module.params.get('vlan_name')
    arista_sw = module.params.get('arista_sw')
    print arista_sw

    eapi_conn = pyeapi.connect_to(arista_sw)

    # Check if VLAN already exists
    check_vlan = check_vlan_exists(eapi_conn, vlan_id)

    if check_vlan:
        if vlan_name is not None and check_vlan != vlan_name:
            configure_vlan(eapi_conn, vlan_id, vlan_name)
            module.exit_json(msg="VLAN already exists, setting VLAN name", changed=True)
        else:
            module.exit_json(msg="VLAN already exists, no action required", changed=False)

    else:
        configure_vlan(eapi_conn, vlan_id, vlan_name)
        module.exit_json(msg="Adding VLAN including vlan_name (if present)", changed=True)

if __name__ == "__main__":
    main()
