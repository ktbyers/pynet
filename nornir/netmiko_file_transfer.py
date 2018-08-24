from nornir.core import InitNornir
from nornir.plugins.tasks.networking import netmiko_file_transfer

from nornir_test.nornir_utilities import nornir_set_creds, std_print


def main():

    # Initialize Nornir object using hosts.yaml and groups.yaml
    brg = InitNornir(config_file="nornir.yml")
    nornir_set_creds(brg)
    test_file = 'test_file9.txt'

    result = brg.run(
        netmiko_file_transfer,
        source_file=test_file,
        dest_file=test_file,
        direction='put',
        num_workers=20,
    )
    std_print(result)


if __name__ == "__main__":
    main()
