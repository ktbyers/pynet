from ncclient import manager
from lxml import etree


if __name__ == "__main__":

    device = {
        "host": "cisco7.domain.com",
        "port": 830,
        "username": "admin",
        "password": "cisco123",
        "hostkey_verify": False,
    }

    with manager.connect(**device) as nconf:
        nc_reply = nconf.get_config(source="running")
        xml_data = etree.tostring(nc_reply.data_ele, pretty_print=True).decode()
        with open("running.xml", "wt") as f:
            f.write(xml_data)
