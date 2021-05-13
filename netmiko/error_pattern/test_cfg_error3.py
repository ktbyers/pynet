from netmiko import ConnectHandler
from netmiko import ConfigInvalidException

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
try:
    output = ssh_conn.send_config_set(config_lines, error_pattern=r"% Invalid input")
except ConfigInvalidException:

    # send_config_set failed so will still be in configuration mode
    ssh_conn.exit_config_mode()

    print("\nAn exception occurred configuring the device...")
    print("Recover configuration!")
    print("-" * 40)

    recover = "bootflash:/base_config.txt"
    cmd = f"configure replace {recover} force revert trigger error"
    recover_out = ssh_conn.send_command(
        cmd, expect_string=r"#", strip_prompt=False, strip_command=False
    )
    print("Output from recovery command:")
    print(recover_out)
    print("-" * 40)
    print()
finally:
    ssh_conn.disconnect()
