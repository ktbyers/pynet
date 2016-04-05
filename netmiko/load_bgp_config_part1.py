#!/usr/bin/env python

from datetime import datetime

from netmiko import ConnectHandler
from my_devices import cisco_ios, cisco_xr, arista_veos


def main():
    device_list = [cisco_ios, cisco_xr, arista_veos]
    start_time = datetime.now()
    print
    for a_device in device_list:
        net_connect = ConnectHandler(**a_device)
        print "{}: {}".format(net_connect.device_type, net_connect.find_prompt())
    print "Time elapsed: {}\n".format(datetime.now() - start_time)


if __name__ == "__main__":
    main()
