import os
from lxml import etree  # noqa
from ncclient import manager
from rich import print
import pdbr  # noqa

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment


def generate_loopback_cfg(j2_vars=None):

    if j2_vars is None:
        j2_vars = {}

    j2_env = Environment(undefined=StrictUndefined, keep_trailing_newline=True)
    j2_env.loader = FileSystemLoader(["."])

    template_file = "loopback_cfg.j2"
    template = j2_env.get_template(template_file)
    return template.render(**j2_vars)


def save_xml(filename, xml_content):
    with open(filename, "w") as f:
        f.write(xml_content)


if __name__ == "__main__":

    device = {
        "host": "3.85.14.166",
        "port": 830,
        "username": "pyclass",
        "password": "bogus",
        "hostkey_verify": False,
    }
    device["password"] = os.environ["PYNET_PASSWORD"]

    with manager.connect(**device) as m:

        # Generate XML
        loopback_vars = {"loopback_number": "1"}
        xml_content = generate_loopback_cfg(loopback_vars)
        add_loopback = xml_content

        # Save out to a file (so we have a record of the config)
        save_xml("loopback_cfg.xml", xml_content)

        # Stage the new loopback configuration on the candidate config.
        nc_reply = m.edit_config(target="candidate", config=add_loopback)
        print(f"\n{nc_reply}\n")

        # Commit the candidate configuration to running config.
        nc_reply = m.commit()
        print(f"\n{nc_reply}\n")
