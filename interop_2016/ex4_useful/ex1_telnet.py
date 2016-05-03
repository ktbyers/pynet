#!/usr/bin/env python
import telnetlib
import time
import getpass


def send_command(remote_conn, cmd):
    '''Send a command down the telnet channel.'''
    cmd = cmd.rstrip()
    remote_conn.write(cmd + '\n')
    time.sleep(1)
    return remote_conn.read_very_eager()

if __name__ == "__main__":
    debug = False
    TELNET_PORT = 23
    TELNET_TIMEOUT = 6

    ip_addr = raw_input("IP address: ")
    ip_addr = ip_addr.strip()
    username = 'pyclass'
    password = getpass.getpass()

    remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
    remote_conn.write(username + '\n')
    output += remote_conn.read_until("ssword:", TELNET_TIMEOUT)
    remote_conn.write(password + '\n')

    time.sleep(1)
    remote_conn.read_very_eager()
    output += send_command(remote_conn, 'terminal length 0')

    if debug:
        print output
    output = send_command(remote_conn, 'show ip int brief')

    print "\n\n"
    print output
    print "\n\n"

    remote_conn.close()

