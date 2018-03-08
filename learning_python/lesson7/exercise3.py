#!/usr/bin/env python
"""
Expand on exercise2 except this time configure both sides of an OSPF session

The output for arista1 should be:

----- arista1 -----
interface Vlan1
   ip ospf priority 100

router ospf 10
   passive-interface default
   no passive-interface Vlan1
   no passive-interface Vlan2
   network 10.10.10.0/24 area 0.0.0.0
   network 10.10.20.0/24 area 0.0.0.0
   network 10.10.30.0/24 area 0.0.0.0
   max-lsa 12000
-------------------

This is identical to what you had as the output for exercise2

The output for arista2 should be:

----- arista2 -----
interface Vlan1
   ip ospf priority 90

router ospf 10
   passive-interface default
   no passive-interface Vlan1
   no passive-interface Vlan2
   no passive-interface Vlan3
   no passive-interface Vlan4
   network 10.10.10.0/24 area 0.0.0.0
   max-lsa 12000
--------------------

You should use identical the same Jinja2 templates for both devices. Ideally you would have one
data structure that contains both the data for 'arista1' and for 'arista2'

# For example:

ospf_params = {
    'arista1': { ospf vars for arista1 },
    'arista2': { ospf vars for arista2 },
}
"""
from __future__ import print_function, unicode_literals
import jinja2

template_file = 'ospf_config.j2'
with open(template_file) as f:
    jinja_template = f.read()

arista1_ospf_active_interfaces = ['Vlan1', 'Vlan2']
arista1_area0_networks = [
    '10.10.10.0/24',
    '10.10.20.0/24',
    '10.10.30.0/24',
]

arista2_ospf_active_interfaces = ['Vlan1', 'Vlan2', 'Vlan3', 'Vlan4']
arista2_area0_networks = [
    '10.10.10.0/24',
]

template_vars = {
    'arista1': {
        'ospf_process_id': 10,
        'ospf_priority': 100,
        'ospf_active_interfaces': arista1_ospf_active_interfaces,
        'ospf_area0_networks': arista1_area0_networks,
    },
    'arista2': {
        'ospf_process_id': 10,
        'ospf_priority': 90,
        'ospf_active_interfaces': arista2_ospf_active_interfaces,
        'ospf_area0_networks': arista2_area0_networks,
    },
}

for switch_name, ospf_vars in template_vars.items():
    template = jinja2.Template(jinja_template)
    print()
    print(switch_name.center(80, '-'))
    print(template.render(ospf_vars))
    print('-' * 80)
    print()
