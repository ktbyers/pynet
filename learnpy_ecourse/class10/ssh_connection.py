import paramiko
import time

def disable_paging(remote_conn, command="terminal length 0\n", delay=1):

    remote_conn.send("\n")
    remote_conn.send(command)

    # Wait for the command to complete
    time.sleep(delay)

    output = remote_conn.recv(65535)

    return output


def establish_connection(ip, username='', password=''):
    '''
    Use Paramiko to establish an SSH channel to the device

    Must return both return_conn_pre and return_conn so that the SSH
    connection is not garbage collected
    
    '''

    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(
        paramiko.AutoAddPolicy())

    remote_conn_pre.connect(ip, username=username, password=password)

    remote_conn = remote_conn_pre.invoke_shell()

    # Clear banner and prompt
    output = remote_conn.recv(65535)

    return (remote_conn_pre, remote_conn, output)


def read_ssh_data(remote_conn, delay=1):
    '''
    Read the data from the ssh channel

    Uses a delay based mechansim
    '''

    # Wait for the command to complete
    time.sleep(delay)
    return remote_conn.recv(65535)


if __name__ == "__main__":

    ip = '10.220.88.1'
    username = 'pynet'
    password = '*'

    (remote_conn_pre, remote_conn, output) = establish_connection(ip, username, password)
    output = disable_paging(remote_conn)

    remote_conn.send("\n")
    remote_conn.send("show version\n")

    output = read_ssh_data(remote_conn)
    print output

    remote_conn_pre.close()
