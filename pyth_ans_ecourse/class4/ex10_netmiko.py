#!/usr/bin/env python
'''
Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx.
Use processes or threads to get this to occur concurrently.
'''

import multiprocessing
from datetime import datetime

from getpass import getpass
from netmiko import ConnectHandler
from netmiko import NetMikoTimeoutException, NetMikoAuthenticationException
from test_devices import pynet1, pynet2, juniper_srx


def print_output(results):
    '''
    Display output
    '''
    print "\nSuccessful devices:"
    for a_dict in results:
        for identifier, val in a_dict.iteritems():
            (success, out_string) = val
            if success:
                print '\n\n'
                print '#' * 80
                print 'Device = {0}\n'.format(identifier)
                print out_string
                print '#' * 80

    print "\n\nFailed devices:\n"
    for a_dict in results:
        for identifier, val in a_dict.iteritems():
            (success, out_string) = val
            if not success:
                print 'Device failed = {0}'.format(identifier)

    print "\nEnd time: " + str(datetime.now())
    print


def worker_cmd(a_device, mp_queue, cmd='show arp'):
    '''
    Return a dictionary where the key is the device identifier
    Value is (success|fail(boolean), return_string)
    '''

    identifier = '{ip}:{port}'.format(**a_device)
    return_data = {}

    try:
        net_connect = ConnectHandler(**a_device)
        output = net_connect.send_command(cmd)
        return_data[identifier] = (True, output)
    except (NetMikoTimeoutException, NetMikoAuthenticationException) as e:
        return_data[identifier] = (False, e)

    # Add data to the queue (for parent process)
    mp_queue.put(return_data)


def main():
    '''
    Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx.
    Use processes or threads to get this to occur concurrently.
    '''
    ip_addr = raw_input("Enter IP address: ")
    password = getpass()

    # Get connection parameters setup correctly
    for a_dict in (pynet1, pynet2, juniper_srx):
        a_dict['ip'] = ip_addr
        a_dict['password'] = password
        a_dict['verbose'] = False
        try:
            a_dict['port']
        except KeyError:
            a_dict['port'] = 22

    mp_queue = multiprocessing.Queue()
    processes = []

    print "\nStart time: " + str(datetime.now())
    for a_device in (pynet1, pynet2, juniper_srx):
        p = multiprocessing.Process(target=worker_cmd, args=(a_device, mp_queue))
        processes.append(p)
        # start the work process
        p.start()

    # wait until the child processes have completed
    for p in processes:
        p.join()

    # retrieve all the data from the queue
    results = []
    for p in processes:
        results.append(mp_queue.get())

    print_output(results)

if __name__ == "__main__":
    main()
