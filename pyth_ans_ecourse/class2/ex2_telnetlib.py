#!/usr/bin/env python
'''
Write a script that connects to the lab pynet-rtr1, logins, and executes the
'show ip int brief' command.
'''

import telnetlib
import time
import socket
import sys
import getpass

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def send_command(remote_conn, cmd):
    '''
    Send a command down the telnet channel

    Return the response
    '''
    cmd = cmd.rstrip()
    remote_conn.write(cmd + '\n')
    time.sleep(1)
    return remote_conn.read_very_eager()

def login(remote_conn, username, password):
    '''
    Login to network device
    '''
    output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
    remote_conn.write(username + '\n')
    output += remote_conn.read_until("ssword:", TELNET_TIMEOUT)
    remote_conn.write(password + '\n')
    return output

def disable_paging(remote_conn, paging_cmd='terminal length 0'):
    '''
    Disable the paging of output (i.e. --More--)
    '''
    return send_command(remote_conn, paging_cmd)

def telnet_connect(ip_addr):
    '''
    Establish telnet connection
    '''
    try:
        return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    except socket.timeout:
        sys.exit("Connection timed-out")


def main():
    '''
    Write a script that connects to the lab pynet-rtr1, logins, and executes the
    'show ip int brief' command.
    '''
    ip_addr = raw_input("IP address: ")
    ip_addr = ip_addr.strip()
    username = 'pyclass'
    password = getpass.getpass()

    remote_conn = telnet_connect(ip_addr)
    output = login(remote_conn, username, password)

    time.sleep(1)
    remote_conn.read_very_eager()
    disable_paging(remote_conn)

    output = send_command(remote_conn, 'show ip int brief')

    print "\n\n"
    print output
    print "\n\n"

    remote_conn.close()

if __name__ == "__main__":
    main()
