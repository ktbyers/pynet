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

    # Initialize Nornir object using hosts.yaml and groups.yaml
    brg = InitNornir(config_file="nornir.yml")
    nornir_set_creds(brg)
    test_file = 'test_file9.txt'

    result = brg.run(
        task=os_upgrade,
        num_workers=20,
    )
    std_print(result)


if __name__ == "__main__":
    main()
