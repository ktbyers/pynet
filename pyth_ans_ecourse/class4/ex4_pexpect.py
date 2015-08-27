#!/usr/bin/env python
'''
Use Pexpect to change the logging buffer size (logging buffered <size>).

Verify this change by examining the output of 'show run'.
'''

import pexpect
import time
from getpass import getpass

def login(ssh_conn):
    '''
    Handle sending password
    '''
    password = getpass()

    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)
    ssh_conn.expect('#')

def find_prompt(ssh_conn):
    '''
    Find the current prompt

    Pexpect is non-greedy which is problematic
    '''
    ssh_conn.send('\n')
    time.sleep(1)
    ssh_conn.expect('#')
    prompt = ssh_conn.before + ssh_conn.after
    return prompt.strip()

def disable_paging(ssh_conn, pattern='#', cmd='terminal length 0'):
    '''
    Disable the paging of output i.e. --More--
    '''
    ssh_conn.sendline(cmd)
    ssh_conn.expect(pattern)

def main():
    '''
    Use Pexpect to change the logging buffer size (logging buffered <size>).

    Verify this change by examining the output of 'show run'.
    '''
    ip_addr = raw_input("Enter IP address: ")
    username = 'pyclass'
    port = 8022

    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    ssh_conn.timeout = 3

    login(ssh_conn)
    prompt = find_prompt(ssh_conn)
    disable_paging(ssh_conn, prompt)

    ssh_conn.sendline('conf t')
    ssh_conn.expect('#')

    ssh_conn.sendline('logging buffer 9000')
    ssh_conn.expect('#')

    ssh_conn.sendline('end')
    ssh_conn.expect(prompt)

    ssh_conn.sendline('show run | inc logging buffer')
    ssh_conn.expect(prompt)

    print '\n>>>>'
    print ssh_conn.before
    print '>>>>\n'

if __name__ == "__main__":
    main()
