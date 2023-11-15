import yaml
from rich import print
from netmiko import ConnectHandler
from datetime import datetime
from pathlib import Path


def read_yaml(filename):
    with open(filename) as f:
        return yaml.safe_load(f)


def print_output(device, output, start_t):
    # Simplify to just the hostname and not the FQDN
    host = device["host"].split(".")[0]
    print(f"Working on device: {host}")
    print("-" * 50)
    current_t = datetime.now()
    # Only show the first line of the output
    print(f"{output.splitlines()[0]} (Timestamp: {current_t - start_t})")
    print("-" * 50)
    print()


def show_version(device):
    """Execute 'show version' on remote device."""
    with ConnectHandler(**device) as conn:
        out = conn.send_command("show version")
    return out


def main(devices):
    start_t = datetime.now()
    print()
    print(f"NUMBER OF DEVICES: {len(devices)}")
    for device in devices:
        output = show_version(device)
        print_output(device, output, start_t)
    print()


if __name__ == "__main__":
    home = Path.home()
    netmiko_devices = ".netmiko.yml"
    inventory = home / netmiko_devices

    # Load a bunch of devices, assumes you have devices store in ~/.netmiko.yml
    # (using Netmiko format)
    devices = []
    devices_and_groups = read_yaml(inventory)
    for k, v in devices_and_groups.items():
        # Devices are type 'dict'; groups are type 'list'
        if isinstance(v, dict):
            devices.append(v)

    print(devices)
    main(devices)
