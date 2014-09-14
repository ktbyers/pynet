'''
https://pynet.twb-tech.com
Applied Python, Class2, Exercise1

Note, you will need to update the IP, SNMP username and keys to use this script.

You will also need to update the sender and recipient in send_notification.
'''

import cPickle as pickle
import os.path

from snmp_helper import snmp_get_oid,snmp_get_oid_v3,snmp_extract
from email_helper import send_mail

from datetime import datetime
    

def obtain_saved_objects(file_name):
    '''
    Read in previously saved objects from a pickle file

    Returns a dict:
    { 
      'device_name': device_object,
      'device_name': device_object,
    }

    '''

    # Check that the pickle file exists
    if not  os.path.isfile(file_name):
        return {}

    # Read in any saved network devices
    net_devices = {}
    with open(file_name, 'r') as f:
        while True:
            try:
                tmp_device = pickle.load(f)
                net_devices[tmp_device.device_name] = tmp_device
            except EOFError:
                break

    return net_devices


def send_notification(net_device):

    current_time = datetime.now()

    sender = 'sender@twb-tech.com'
    recipient = 'recipient@twb-tech.com'
    subject = 'Device {0} was modified'.format(net_device.device_name)

    message = '''
The running configuration of {0} was modified.  

This change was detected at: {1}

'''.format(net_device.device_name, current_time)

    if send_mail(recipient, subject, message, sender):
        print 'Email notification sent to {}'.format(recipient)
        return True


class NetworkDevice(object):
    '''
    Simple object to store network device information

    For an alternate solution, you could replace the class/objects with 
    a data structure that uses dictionaries.
    '''

    def __init__(self, device_name, uptime, last_changed, config_changed=False):
        self.device_name = device_name
        self.uptime = uptime

        # The uptime value in hundredths of seconds when running configuration
        # was last changed
        self.last_changed = last_changed
        self.run_config_changed = config_changed


def main():
    '''

    Check if the running-configuration has changed, send an email notification when
    this occurs.

    Logic for detecting the running-config has changed:

        Normal (non-reboot):

            # Did ccmHistoryRunningLastChanged increase
            if ccmHistoryRunningLastChanged > network_device_object.last_changed:
                config_changed = True

        Reboot case:

            ccmHistoryRunningLastChanged decreases (i.e. < network_device_object.last_changed)

            Right after reboot, ccmHistoryRunningLastChanged is updated upon
            load of running-config from startup-config.

            Create a grace window (RELOAD_WINDOW) for values of ccmHistoryRunningLastChanged.
            In other words as long as ccmHistoryRunningLastChanged is <= RELOAD_WINDOW assume
            no running-config changes.

            If ccmHistoryRunningLastChanged is > RELOAD_WINDOW assume running-config was changed

    '''

    DEBUG = True

    # 300 seconds (converted to hundredths of seconds)
    RELOAD_WINDOW = 300 * 100

    # Uptime when running config last changed
    ccmHistoryRunningLastChanged = '1.3.6.1.4.1.9.9.43.1.1.1.0'
    # Uptime when run-config last saved (note 'write term/show run' constitutes a save)
    ccmHistoryRunningLastSaved = '1.3.6.1.4.1.9.9.43.1.1.2.0'
    # Uptime when start config last saved
    ccmHistoryStartupLastChanged = '1.3.6.1.4.1.9.9.43.1.1.3.0'

    # Pickle file for storing previous RunningLastChanged timestamp
    net_dev_file = 'netdev.pkl'

    # SNMPv3 Connection Parameters
    IP = '1.1.1.1'
    a_user = 'username'
    auth_key = '*********'
    encrypt_key = '**********'
    snmp_user = (a_user, auth_key, encrypt_key)
    pynet_rtr1 = (IP, 7961)
    pynet_rtr2 = (IP, 8061)

    # Relevant SNMP OIDs
    sysName = '1.3.6.1.2.1.1.5.0'
    sysUptime = '1.3.6.1.2.1.1.3.0'


    print '\n*** Checking for device changes ***'

    saved_devices = obtain_saved_objects(net_dev_file)
    print "{0} devices were previously saved\n".format(len(saved_devices))

    # Temporarily store the current devices in a dictionary
    current_devices = {}

    # Connect to each device / retrieve last_changed time
    for a_device in (pynet_rtr1, pynet_rtr2):
    
        # obtain device_name
        snmp_data = snmp_get_oid_v3(a_device, snmp_user, oid=sysName)
        device_name = snmp_extract(snmp_data)

        snmp_data = snmp_get_oid_v3(a_device, snmp_user, oid=sysUptime)
        uptime = snmp_extract(snmp_data)

        # obtain last_changed time 
        snmp_data = snmp_get_oid_v3(a_device, snmp_user, oid=ccmHistoryRunningLastChanged)
        last_changed = snmp_extract(snmp_data)

        if DEBUG: 
            print "\nConnected to device = {0}".format(device_name)
            print "Last changed timestamp = {0}".format(last_changed)
            print "Uptime = {0}".format(uptime)


        # see if this device has been previously saved
        if device_name in saved_devices:

            saved_device = saved_devices[device_name]
            print "{0} {1}".format(device_name, (35 - len(device_name))*'.'),

            # Check for a reboot (did uptime decrease or last_changed decrease?)
            if uptime < saved_device.uptime or last_changed < saved_device.last_changed:

                if last_changed <= RELOAD_WINDOW:
                    print "DEVICE RELOADED...not changed"
                    current_devices[device_name] = NetworkDevice(device_name, uptime, last_changed, False)
                else:
                    print "DEVICE RELOADED...and changed"
                    current_devices[device_name] = NetworkDevice(device_name, uptime, last_changed, True)
                    send_notification(current_devices[device_name])

            # running-config last_changed is the same
            elif last_changed == saved_device.last_changed:
                print "not changed"
                current_devices[device_name] = NetworkDevice(device_name, uptime, last_changed, False)

            # running-config was modified
            elif last_changed > saved_device.last_changed:
                print "CHANGED"
                current_devices[device_name] = NetworkDevice(device_name, uptime, last_changed, True)
                send_notification(current_devices[device_name])

            else:
                raise ValueError()

        else:
            # New device, just save it
            print "{0} {1}".format(device_name, (35 - len(device_name))*'.'),
            print "saving new device"
            current_devices[device_name] = NetworkDevice(device_name, uptime, last_changed, False)


    # Write the devices to pickle file
    with open(net_dev_file, 'w') as f:
        for dev_obj in current_devices.values():
            pickle.dump(dev_obj, f)

    print


if __name__ == '__main__':

    main()
