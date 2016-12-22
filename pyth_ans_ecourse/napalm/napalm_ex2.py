#!/usr/bin/env python
from pprint import pprint as pp

from napalm_base import get_network_driver
from my_devices import pynet_rtr1

def main():
    for a_device in (pynet_rtr1,):
        device_type = a_device.pop('device_type')
        driver = get_network_driver(device_type)
        device = driver(**a_device)

        print
        print ">>>Device open"
        device.open()

        print
        print ">>>Load config change (merge) - no commit"
        device.load_merge_candidate(filename='cisco_merge.txt')
        print device.compare_config()

        print
        print ">>>Discard config change (merge)"
        device.discard_config()
        print device.compare_config()

        print
        print ">>>Load config change (merge) - commit"
        device.load_merge_candidate(filename='cisco_merge.txt')
        print device.compare_config()
        device.commit_config()

    print

if __name__ == "__main__":
    main()
