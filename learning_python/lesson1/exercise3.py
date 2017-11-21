"""
Create four different variables the first using all lower case with _ as the word separator.

The second with all upper case with _ as the word separator

The third with numbers, letters, and _ (but still a valid variable name)

Make all three variables refer to strings

Use the from future technique so that any string literals are unicode in PY2

compare if ipv6_addr1 equals ipv6_addr2
"""
from __future__ import unicode_literals

ipv6_addr1 = "2001:db8:1234::1"
IPV6_ADDR2 = "2001:db8:1234::2"
ipV6_addR3 = "2001:db8:1234::3"

print(ipv6_addr1 == IPV6_ADDR2)
print(ipv6_addr1 != ipV6_addR3)
