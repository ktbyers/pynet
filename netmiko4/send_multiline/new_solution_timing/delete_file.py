from getpass import getpass
from netmiko import ConnectHandler

device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_ios",
}

with ConnectHandler(**device) as net_connect:

    filename = "test-bp.txt"
    cmd_list = [f"del flash:/{filename}", "\n", "y"]

    output = net_connect.send_multiline_timing(cmd_list)
    print(output)
