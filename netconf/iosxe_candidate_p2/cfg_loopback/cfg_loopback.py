import os
from lxml import etree  # noqa
from ncclient import manager
from rich import print
import pdbr  # noqa


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

        # Read the Loopback CFG XML from a file
        filename = "loopback_cfg.xml"
        with open(filename) as f:
            add_loopback = f.read()

        # Stage the new loopback configuration on the candidate config.
        nc_reply = m.edit_config(target="candidate", config=add_loopback)
        print(f"\n{nc_reply}\n")

        # Commit the candidate configuration to running config.
        nc_reply = m.commit()
        print(f"\n{nc_reply}\n")
