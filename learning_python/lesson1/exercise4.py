"""
Create a show_version variable that contains the following

Remove all leading and trailing whitespace from the string.

Split the string and extract the model and serial_number from it

check if 'Cisco' is in the model string (don't care about capitalization).

check if 881 is in the model number

print out the serial number and the model
"""


show_version = "*0  	  CISCO881-SEC-K9       FTX0000038X    " 
show_version = show_version.strip()
fields = show_version.split()

model = fields[1]
serial_number = fields[2]

print()
print(model)
print(serial_number)

vendor_cisco = 'cisco' in model.lower()
print("Checking if model contains Cisco: {}".format(vendor_cisco))

model_881 = '881' in model
print("Checking if model contains 881: {}".format(model_881))
print()
