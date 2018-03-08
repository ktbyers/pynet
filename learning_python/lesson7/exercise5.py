#!/usr/bin/env python
"""
Define the following variables in a YAML file

  1 Do an exercise where you store certain variables in YAML and then read them
  2 in as variables for your jinja2 templates.
  3 
  4 Make host specific variables that need to be change across time.
"""
from __future__ import print_function, unicode_literals
import jinja2

template_file = 'ospf_config.j2'
with open(template_file) as f:
    jinja_template = f.read()
