import telnetlib
import time

TELNET_PORT = 23
TELNET_TIMEOUT = 6
READ_TIMEOUT = 6

def disable_paging(remote_conn, command="terminal length 0\n", delay=1):
    '''
    Disable router paging i.e. --More--

    Returns the output buffer
    '''

    remote_conn.write("terminal length 0\n")
    time.sleep(delay)
    return remote_conn.read_very_eager()

def establish_connection(ip, username='', password='', delay=1):
    '''
    Establish the telnet connection and login
    '''

    remote_conn = telnetlib.Telnet(ip, TELNET_PORT, TELNET_TIMEOUT)

    output = remote_conn.read_until("sername:", READ_TIMEOUT)
    remote_conn.write(username + "\n")

    output = remote_conn.read_until("ssword:", READ_TIMEOUT)
    remote_conn.write(password + "\n")

    time.sleep(delay)

    return remote_conn


if __name__ == "__main__":

    ip = '10.220.88.1'
    username = 'pynet'
    password = '*'

    remote_conn = establish_connection(ip, username, password)

    output = disable_paging(remote_conn)

    remote_conn.write("\n")
    remote_conn.write("show version\n")

    time.sleep(1)
    output = remote_conn.read_very_eager()
    print output

    remote_conn.close()
