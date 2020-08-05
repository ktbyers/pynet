#!/usr/bin/env python
"""
Use Jinja2 templating to render the following:

vlan {{ vlan_id }}
   name {{ vlan_name }}


Your template should be inside of your Python program for simplicity.


The output from processing your template should be as follows. This should be printed to stdout.

vlan 400
   name red400

"""
from __future__ import print_function, unicode_literals
import jinja2

template_vars = {
    "vlan_id": 400,
    "vlan_name": "red400",
}

vlan_template = """
vlan {{ vlan_id }}
   name {{ vlan_name }}

"""

template = jinja2.Template(vlan_template)
print(template.render(template_vars))
