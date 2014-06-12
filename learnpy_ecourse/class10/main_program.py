'''

This is a solution to the below problem given the content we have
discussed in class.  It is not necessarily the best solution to the problem.
In other words, I generally only use things we have covered up to this point
in the class (with some exceptions which I will usually note). 

Python for Network Engineers
https://pynet.twb-tech.com
Learning Python


Create a script that can login to a network device (using either telnet or SSH) 
and retrieve 'show version' from the device.  

Process the 'show version' output and store the below attributes in a 
NetworkDevice object:

NetworkObject
    hostname
    ip
    username    
    password 
    device_type          # router, switch, firewall, etc.
    vendor
    model
    os_version
    uptime               # seconds
    serial_number


This object should be stored to a file using pickle. 


Here is the output of running essentially this code against a test device 
(password stripped):

$ python main_program.py 

Using SSH:
       hostname: twb-sf-881                              
             ip: 10.220.88.1                             
       username: pynet                                   
       password: *
    device_type: router                                  
         vendor: Cisco                                   
          model: 881                                     
     os_version: 15.0(1)M4                               
         uptime: 8978280                                 
  serial_number: FTX1512038X                             

Using telnet:
       hostname: twb-sf-881                              
             ip: 10.220.88.1                             
       username: pynet                                   
       password: *
    device_type: router                                  
         vendor: Cisco                                   
          model: 881                                     
     os_version: 15.0(1)M4                               
         uptime: 8978280                                 
  serial_number: FTX1512038X                             



Reading objects from pickle files:
       hostname: twb-sf-881                              
             ip: 10.220.88.1                             
       username: pynet                                   
       password: *
    device_type: router                                  
         vendor: Cisco                                   
          model: 881                                     
     os_version: 15.0(1)M4                               
         uptime: 8978280                                 
  serial_number: FTX1512038X                             

       hostname: twb-sf-881                              
             ip: 10.220.88.1                             
       username: pynet                                   
       password: *
    device_type: router                                  
         vendor: Cisco                                   
          model: 881                                     
     os_version: 15.0(1)M4                               
         uptime: 8978280                                 
  serial_number: FTX1512038X                             

'''


import time
import pickle

import ssh_connection as ssh
import telnet_connection as telnet
from show_version_parser import process_show_version


class NetworkDevice(object):
    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password


def ssh_main():
    '''
    Process show version using SSH
    '''

    ip = '10.220.88.1'
    username = 'pynet'
    password = '*'

    test_device = NetworkDevice(ip, username, password)

    (remote_conn_pre, remote_conn, output) = ssh.establish_connection(ip, username, password)
    output = ssh.disable_paging(remote_conn)

    remote_conn.send("\n")
    remote_conn.send("show version\n")

    # Read the output from the 'show version' command
    test_device.show_version = ssh.read_ssh_data(remote_conn)

    remote_conn_pre.close()
    process_show_version(test_device)

    # Print to stdout for verification
    net_device_verification(test_device)

    # Write object to a file
    with open('ssh_file.pkl', 'wb') as f:
        pickle.dump(test_device, f)


def telnet_main():
    '''
    Process show version using telnet
    '''

    ip = '10.220.88.1'
    username = 'pynet'
    password = '*'

    test_device2 = NetworkDevice(ip, username, password)

    remote_conn = telnet.establish_connection(ip, username, password)

    telnet.disable_paging(remote_conn)

    remote_conn.write("\n")
    remote_conn.write("show version\n")

    time.sleep(1)
    test_device2.show_version = remote_conn.read_very_eager()

    remote_conn.close() 
    process_show_version(test_device2)

    # Print to stdout for verification
    net_device_verification(test_device2)

    # Write object to a file
    with open('telnet_file.pkl', 'wb') as f:
        pickle.dump(test_device2, f)


def net_device_verification(net_device):
    '''
    Prints out a set of attributes for a NetworkDevice object
    '''

    print_attr = [    
        'hostname',
        'ip',
        'username',
        'password',
        'device_type',
        'vendor',
        'model',
        'os_version',
        'uptime',
        'serial_number',
    ]

    # Uses getattr to get the right attribute
    for field in print_attr:
        val = getattr(net_device, field)
        print "%15s: %-40s" % (field, val)

    print

if __name__ == "__main__":

    print
    print "Using SSH:"
    ssh_main()

    print "Using telnet:"
    telnet_main()

    print "\n"
    print "Reading objects from pickle files:"
    my_files = ['ssh_file.pkl', 'telnet_file.pkl']
    for a_file in my_files:
        with open(a_file, 'rb') as f:
            netdev_obj = pickle.load(f)
            net_device_verification(netdev_obj)

