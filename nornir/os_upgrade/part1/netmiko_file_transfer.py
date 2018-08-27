from nornir.core import InitNornir
from nornir.plugins.tasks.networking import netmiko_file_transfer

from nornir_utilities import nornir_set_creds, std_print


# Initialize Nornir object using hosts.yaml and groups.yaml
norn = InitNornir(config_file="nornir.yml")
nornir_set_creds(norn)
test_file = 'test_file4.txt'

result = norn.run(
    task=netmiko_file_transfer,
    source_file=test_file,
    dest_file=test_file,
    direction='put',
    num_workers=20,
)
std_print(result)
