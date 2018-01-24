from pprint import pprint
import os

# Toggle this to use Windows
WINDOWS = False

base_ip = '8.8.4.'
base_cmd_linux = 'ping -c 2'
base_cmd_windows = 'ping -n 2'
# Ternary operator
base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux

ip_list = []
for last_octet in range(1, 255):
    new_ip = base_ip + str(last_octet)
    ip_list.append(new_ip)

for i, ip_addr in enumerate(ip_list):
    print("{} ---> {}".format(i, ip_addr))

ip_list = ip_list[2:6]

if '8.8.4.4' in ip_list:
    print("FOUND 8.8.4.4")
else:
    print("FAILED")

print('-' * 80)
for ip_addr in ip_list:
    if '8.8.4.0' == ip_addr:
        continue
    print("IP Addr: ", ip_addr)
    return_code = os.system("ping -c 3 {}".format(ip_addr))
    print('-' * 80)
