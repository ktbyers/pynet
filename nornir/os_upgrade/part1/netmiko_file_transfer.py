from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_file_transfer

from nornir_utilities import nornir_set_creds, std_print


# Initialize Nornir object using default "SimpleInventory" plugin 
nr = InitNornir()
nornir_set_creds(nr)
test_file = 'test_file4.txt'

result = nr.run(
    task=netmiko_file_transfer,
    source_file=test_file,
    dest_file=test_file,
    direction='put',
    num_workers=20,
)
std_print(result)
