from getpass import getpass
from netmiko import ConnectHandler

device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_xe",
}

with ConnectHandler(**device) as net_connect:

"""
​cisco3#ping
Protocol [ip]: 
Target IP address: 8.8.8.8
Repeat count [5]: 30
Datagram size [100]: 
Timeout in seconds [2]: 
Extended commands [n]: 
Sweep range of sizes [n]: 
Type escape sequence to abort.
Sending 30, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Success rate is 100 percent (30/30), round-trip min/avg/max = 1/2/4 ms
cisco3#
"""

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
    print(output)
