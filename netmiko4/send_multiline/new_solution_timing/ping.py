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
    """
    # Example from CLI
    cisco3#ping
    Protocol [ip]:
    Target IP address: 8.8.8.8
    Repeat count [5]: 30
    Datagram size [100]:
    Timeout in seconds [2]:
    Extended commands [n]:
    Sweep range of sizes [n]:
    """
    target_ip = "8.8.8.8"
    count = "30"
    cmd_list = [
        "ping",
        "\n",
        target_ip,
        count,
        "\n",
        "\n",
        "\n",
        "\n",
    ]

    output = net_connect.send_multiline_timing(cmd_list)
    print(output)
