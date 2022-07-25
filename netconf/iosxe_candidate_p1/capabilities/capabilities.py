from ncclient import manager
from rich import print


if __name__ == "__main__":

    device = {
        "host": "cisco7.domain.com",
        "port": 830,
        "username": "admin",
        "password": "cisco123",
        "hostkey_verify": False,
    }

    with manager.connect(**device) as nconf:
        print(list(nconf.server_capabilities))
