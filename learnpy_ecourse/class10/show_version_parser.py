import re
from uptime import Uptime

def process_show_version(net_device):
    '''
    Process the show_version output for net_device

    Assign the following attributes to the net_device object

    hostname
    device_type          # router, switch, firewall, etc.
    vendor
    model
    os_version
    uptime               # seconds
    serial_number

    '''

    show_ver = net_device.show_version

    # Process show_version output
    net_device.vendor, net_device.model = obtain_vendor_model(show_ver)
    net_device.os_version = obtain_os_version(show_ver)
    net_device.uptime = obtain_uptime(show_ver)
    net_device.hostname = obtain_hostname(show_ver)
    net_device.serial_number = obtain_serial_number(show_ver)
    net_device.device_type = obtain_device_type(net_device.model)


def obtain_vendor_model(show_ver):

    # '(.+?) ' means any sequence of one or more characters followed by space (shortest match)
    match = re.search(r"Cisco (.+?) .+bytes of memory", show_ver)
    if match:
        return ("Cisco", match.group(1))
    else:
        return None

def obtain_os_version(show_ver):

    # (.+?), means any sequence of one or more characters followed by comma (shortest match)
    match = re.search(r"Cisco IOS Software.*Version (.+?),", show_ver)
    if match:
        return match.group(1)
    else:
        return None

def obtain_uptime(show_ver):

    match = re.search(r".* uptime is .*", show_ver)

    if match:
        uptime_str = match.group().strip()
        uptime_obj = Uptime(uptime_str)
        return uptime_obj.uptime_seconds()
    else:
        return None

def obtain_hostname(show_ver):
    '''
    Example string from Cisco IOS:
    twb-sf-881 uptime is 14 weeks, 4 days, 22 hours, 59 minutes
    
    return the hostname, else None
    '''

    match = re.search(r"(.+) uptime is .+", show_ver)
    if match:
        return match.group(1)
    else:
        return None

def obtain_serial_number(show_ver):
    '''
    Example string from Cisco IOS:
    Processor board ID FTX1000008X

    return the serial_number, else None
    '''

    match = re.search(r"Processor board ID (.+)", show_ver)
    if match:
        return match.group(1).strip()
    else:
        return None

def obtain_device_type(model):
    '''
    Determine the device_type based on the model
    '''

    if '881' in model:
        return 'router'
    else:
        return None

