import re


def onepk_find_model(part_number):
    
    if 'CISCO881' in part_number:
        return '881'
    else:
        raise ValueError("Unable to find model from part number({})".format(part_number))

def onepk_find_device_type(model):

    if model == '881':
        return 'router'
    else:
        raise ValueError("Unable to find device_type from model({})".format(model))

def onepk_find_os_version(sys_descr):

    match = re.search(r'Cisco IOS Software, (.*)', sys_descr)
    if match:
        return match.group(1)
    else:
        raise ValueError("Unable to find IOS version from sys_descr({})".format(sys_descr))
 
