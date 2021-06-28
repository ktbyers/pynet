from getpass import getpass
from netmiko import ConnectHandler

device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
}

with ConnectHandler(**device) as net_connect:

    cmd = "ping"
    target_ip = "8.8.8.8"
    count = "30"

    output = net_connect.send_command_timing(
        cmd, strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command_timing(
        "\n", strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command_timing(
        target_ip, strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command_timing(
        count, strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command_timing(
        "\n", strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command_timing(
        "\n", strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command_timing(
        "\n", strip_prompt=False, strip_command=False
    )
    output += net_connect.send_command_timing(
        "\n", strip_prompt=False, strip_command=False
    )
    print(output)
