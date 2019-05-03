import re
import sys

from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_file_transfer
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.tasks.networking import netmiko_send_config

from nornir_utilities import nornir_set_creds, std_print


def os_upgrade(task):
    file_name = task.host.get('img')
    task.run(
        task=netmiko_file_transfer,
        source_file=file_name,
        dest_file=file_name,
        direction='put',
    )
    return ""


def set_boot_var(task):
    """
    Set the boot variable for Cisco IOS.

    return True if boot variable set

    return False if staging verification steps failed (i.e. before the boot variable was set).
    """
    primary_img = task.host.get('img')
    backup_img = task.host.get('backup_img')

    # Check images are on the device
    for img in (primary_img, backup_img):
        result = task.run(
            task=netmiko_send_command,
            command_string=f"dir flash:/{img}"
        )
        output = result[0].result
        # Drop the first line as that line always contains the filename
        output = re.split(r"Directory of.*", output, flags=re.M)[1]
        if img not in output:
            return False

    commands = f"""
default boot system
boot system flash {primary_img}
boot system flash {backup_img}
"""
    command_list = commands.strip().splitlines()
    task.run(
        task=netmiko_send_config,
        config_commands=command_list
    )
    return True


def continue_func(msg="Do you want to continue (y/n)? "):
    response = input(msg).lower()
    if 'y' in response:
        return True
    else:
        sys.exit()


def main():
    # Initialize Nornir object using default "SimpleInventory" plugin
    nr = InitNornir()
    nornir_set_creds(nr)
    result = nr.run(
        task=os_upgrade,
        num_workers=20,
    )
    std_print(result)

    # Filter to only a single device
    nr_ios = nr.filter(hostname="cisco1.domain.com")

    aggr_result = nr_ios.run(task=set_boot_var)

    # If setting the boot variable failed (assumes single device at this point)
    for hostname, val in aggr_result.items():
        if val[0].result is False:
            sys.exit("Setting the boot variable failed")

    # Verify the boot variable
    result = nr_ios.run(
        task=netmiko_send_command,
        command_string="show run | section boot",
        num_workers=20,
    )
    std_print(result)
    continue_func()

    # Save the config
    result = nr_ios.run(
        task=netmiko_send_command,
        command_string="write mem",
    )
    std_print(result)

    # Reload
    continue_func(msg="Do you want to reload the device (y/n)? ")
    result = nr_ios.run(
        task=netmiko_send_command,
        use_timing=True,
        command_string="reload",
    )

    # Confirm the reload (if 'confirm' is in the output)
    for device_name, multi_result in result.items():
        if 'confirm' in multi_result[0].result:
            result = nr_ios.run(
                task=netmiko_send_command,
                use_timing=True,
                command_string="y",
            )

    print("Devices reloaded")


if __name__ == "__main__":
    main()
