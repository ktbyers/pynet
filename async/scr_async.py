import asyncio
import yaml
from rich import print
from scrapli import AsyncScrapli
from pathlib import Path


def read_yaml(filename):
    with open(filename) as f:
        return yaml.safe_load(f)


def scraplifi(device_dict):
    """Convert over to Scrapli dict format from Netmiko format."""
    scrapli_dict = {
        "auth_strict_key": False,
        "transport": "asyncssh",
    }
    for k, v in device_dict.items():
        if k == "username":
            scrapli_dict["auth_username"] = v
        elif k == "password":
            scrapli_dict["auth_password"] = v
        elif k == "device_type":
            if v in ["cisco_xe", "cisco_ios"]:
                v = "cisco_iosxe"
            scrapli_dict["platform"] = v
        elif k == "global_delay_factor":
            continue
        else:
            scrapli_dict[k] = v

    return scrapli_dict


async def show_version(device):
    """Async execution of 'show version' on remote device."""
    conn = AsyncScrapli(**device)
    await conn.open()

    res = await conn.send_command("show version")
    await conn.close()
    return res


async def main(devices):
    remote_work = (show_version(d) for d in devices)
    # import pdbr; pdbr.set_trace()
    results = await asyncio.gather(*remote_work)
    for res in results:
        host = res.host
        host = host.split(".")[0]
        print()
        print(f"Results for host: {host}")
        print("-" * 50)
        print(f"{res.result.splitlines()[0]}")
        print("-" * 50)
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
        if isinstance(v, dict):
            device_dict = scraplifi(v)
            devices.append(device_dict)

    asyncio.run(main(devices))
