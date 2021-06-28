from getpass import getpass
from netmiko import ConnectHandler

device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_xe",
}

with ConnectHandler(**device) as net_connect:

    filename = "reubens_lesson9_config.txt"
    cmd = f"del flash:/{filename}"

    output = net_connect.send_command_timing(
        cmd, strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command_timing(
        "\n", strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command_timing(
        "y", strip_prompt=False, strip_command=False
    )
    print(output)
