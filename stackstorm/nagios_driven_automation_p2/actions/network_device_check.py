import sys
from st2common.runners.base_action import Action
from nornir import InitNornir
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


__all__ = ["NetDevAlive"]

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class NetDevAlive(Action):
    def run(self, down_device):
        print(f"Checking to see if device {down_device} is alive...")

        nr = InitNornir(
            config_file="/opt/stackstorm/packs/super_cool_python/nornir/config.yaml"
        )
        nr = nr.filter(name=f"{down_device.split('.')[0]}")
        result = True
        try:
            print(f"Trying netmiko connection to device {down_device}...")
            nr.inventory.hosts[f"{down_device.split('.')[0]}"].open_connection(
                "netmiko", None
            )
            conn = (
                nr.inventory.hosts[f"{down_device.split('.')[0]}"]
                .connections["netmiko"]
                .connection
            )
            conn.find_prompt()
            print(f"Successfully opened netmiko connection to device {down_device}...")
        except Exception as e:
            print(f"Encounted error opening netmiko connection to device. Error: {e}")
            result = False
        try:
            print(f"Trying napalm connection to device {down_device}...")
            nr.inventory.hosts[f"{down_device.split('.')[0]}"].open_connection(
                "napalm", None
            )
            conn = (
                nr.inventory.hosts[f"{down_device.split('.')[0]}"]
                .connections["napalm"]
                .connection
            )
            conn.open()
            print(f"Successfully opened napalm connection to device {down_device}...")
        except Exception as e:
            print(f"Encounted error opening napalm connection to device. Error: {e}")
            result = False

        print(f"Device {down_device} is alive?: {result}")
        if not result:
            sys.exit(1)
        return result
