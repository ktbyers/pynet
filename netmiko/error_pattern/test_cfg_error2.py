from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "cisco5.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
}

config_lines = [
    "logging buffered 20000 critical",
    "no logging console",
    "bad command",
    "ntp server 130.126.24.24",
    "ntp server 152.2.21.1",
]

ssh_conn = ConnectHandler(**device)
output = ssh_conn.send_config_set(config_lines, error_pattern=r"% Invalid input")
print(output)
ssh_conn.disconnect()
