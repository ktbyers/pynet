#!/usr/bin/env python

from datetime import datetime

from netmiko import ConnectHandler
from my_devices import cisco_ios, cisco_xr, arista_veos


def check_bgp(net_connect, cmd='show run | inc router bgp'):
    """Check whether BGP is currently configured on device. Return boolean"""
    output = net_connect.send_command_expect(cmd)
    return 'bgp' in output

def remove_bgp_config(net_connect, cmd='no router bgp', as_number=''):
    """Remove BGP from the config"""
    bgp_cmd = "{} {}".format(cmd, str(as_number))
    cmd_list = [bgp_cmd]
    output = net_connect.send_config_set(cmd_list)
    if net_connect.device_type == 'cisco_xr_ssh':
        output += net_connect.commit()
    print output

def configure_bgp(net_connect, file_name=''):
    """Configure BGP on device."""
    try:
        output = net_connect.send_config_from_file(config_file=file_name)
        if net_connect.device_type == 'cisco_xr_ssh':
            output += net_connect.commit()
        return output
    except IOError:
        print "Error reading file: {}".format(file_name)

def main():
    device_list = [cisco_ios, cisco_xr, arista_veos]
    start_time = datetime.now()
    print

    for a_device in device_list:
        as_number = a_device.pop('as_number')
        net_connect = ConnectHandler(**a_device)
        net_connect.enable()
        print "{}: {}".format(net_connect.device_type, net_connect.find_prompt())
        if check_bgp(net_connect):
            print "BGP currently configured"
            remove_bgp_config(net_connect, as_number=as_number)
        else:
            print "No BGP"

        # Check BGP is now gone
        if check_bgp(net_connect):
            raise ValueError("BGP configuration still detected")

        # Construct file_name based on device_type
        device_type = net_connect.device_type
        file_name = 'bgp_' + device_type.split("_ssh")[0] + '.txt'

        # Configure BGP
        output = configure_bgp(net_connect, file_name)
        print output
        print

    print "Time elapsed: {}\n".format(datetime.now() - start_time)


if __name__ == "__main__":
    main()
