from getpass import getpass
from netmiko import ConnectHandler

device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_ios",
}

with ConnectHandler(**device) as net_connect:

    filename = "test9-dp.txt"
    cmd_list = [
        [f"del flash:/{filename}", r"Delete filename"],
        ["\n", r"confirm"],
        ["y", ""],
    ]

    output = net_connect.send_multiline(cmd_list)
    print(output)
