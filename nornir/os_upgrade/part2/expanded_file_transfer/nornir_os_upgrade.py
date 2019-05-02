from nornir.core import InitNornir
from nornir.plugins.tasks.networking import netmiko_file_transfer

from nornir_test.nornir_utilities import nornir_set_creds, std_print


def os_upgrade(task):
    file_name = task.host.get('img')
    result = task.run(
        task=netmiko_file_transfer,
        source_file=file_name,
        dest_file=file_name,
        direction='put',
    )
    return result


def main():
    # Initialize Nornir object using default "SimpleInventory" plugin
    nr = InitNornir()
    nornir_set_creds(nr)
    result = nr.run(
        task=os_upgrade,
        num_workers=20,
    )
    std_print(result)


if __name__ == "__main__":
    main()
