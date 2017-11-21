"""
You have the following three variables from an arp table:

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

print out a tabular output that looks like this using the format method
"""

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

fields = mac1.split()
ip_addr1 = fields[1]
mac1 = fields[3]
print(ip_addr1, mac1)

fields = mac2.split()
ip_addr2 = fields[1]
mac2 = fields[3]
print(ip_addr2, mac2)

fields = mac3.split()
ip_addr3 = fields[1]
mac3 = fields[3]
print(ip_addr3, mac3)

print()
print("{:>20} {:>20}".format("IP ADDR", "MAC ADDRESS"))
print("{:>20} {:>20}".format("-" * 20, "-" * 20))
print("{:>20} {:>20}".format(ip_addr1, mac1))
print("{:>20} {:>20}".format(ip_addr2, mac2))
print("{:>20} {:>20}".format(ip_addr3, mac3))
print()
