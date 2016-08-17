#!/usr/bin/env python
'''
Use Paramiko to retrieve the entire 'show version' output.
'''

import paramiko
import time
from getpass import getpass

MAX_BUFFER = 65535

def clear_buffer(remote_conn):
    '''
    Clear any data in the receive buffer
    '''
    if remote_conn.recv_ready():
        return remote_conn.recv(MAX_BUFFER)

def disable_paging(remote_conn, cmd='terminal length 0'):
    '''
    Disable output paging (i.e. --More--)
    '''
    cmd = cmd.strip()
    remote_conn.send(cmd + '\n')
    time.sleep(1)
    clear_buffer(remote_conn)

def send_command(remote_conn, cmd='', delay=1):
    '''
    Send command down the channel. Retrieve and return the output.
    '''
    if cmd != '':
        cmd = cmd.strip()
    remote_conn.send(cmd + '\n')
    time.sleep(delay)

    if remote_conn.recv_ready():
        return remote_conn.recv(MAX_BUFFER)
    else:
        return ''

def main():
    '''
    Use Paramiko to retrieve the entire 'show version' output.
    '''
    ip_addr = raw_input("Enter IP address: ")
    username = 'pyclass'
    password = getpass()
    port = 22

    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.load_system_host_keys()

    remote_conn_pre.connect(ip_addr, port=port, username=username, password=password,
                            look_for_keys=False, allow_agent=False)
    remote_conn = remote_conn_pre.invoke_shell()

    time.sleep(1)
    clear_buffer(remote_conn)
    disable_paging(remote_conn)

    output = send_command(remote_conn, cmd='show version')
    print '\n>>>>'
    print output
    print '>>>>\n'

if __name__ == "__main__":
    main()
