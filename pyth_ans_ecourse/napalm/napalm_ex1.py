#!/usr/bin/env python
from pprint import pprint as pp

from napalm_base import get_network_driver
from my_devices import device_list

def main():
    for a_device in device_list:
        device_type = a_device.pop('device_type')
        driver = get_network_driver(device_type)
        device = driver(**a_device)

        print
        print ">>>Device open"
        device.open()

        print "-" * 50
        device_facts = device.get_facts()
        print "{hostname}: Model={model}".format(**device_facts)

    print

if __name__ == "__main__":
    main()
