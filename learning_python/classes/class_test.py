import paramiko
from getpass import getpass
import time


class SSHConn:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

    def open(self):
        remote_conn_pre = paramiko.SSHClient()
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        remote_conn_pre.connect(
            self.host,
            username=self.username,
            password=self.password,
            look_for_keys=False,
            allow_agent=False,
        )
        remote_conn = remote_conn_pre.invoke_shell()
        self.remote_conn_pre = remote_conn_pre
        self.ssh_conn = remote_conn

    def verify_connection(self):
        self.ssh_conn.send("\n\n")
        time.sleep(1)
        return self.ssh_conn.recv(20000).decode()

    def disable_paging(self, cmd="terminal length 0\n"):
        self.ssh_conn.send(cmd)
        time.sleep(1)
        return self.ssh_conn.recv(2000).decode()


if __name__ == "__main__":

    # Establish connection
    password = getpass()
    my_conn = SSHConn(host="cisco1.lasthop.io", username="pyclass", password=password)
    my_conn.open()

    # Verify connection
    output = my_conn.verify_connection()
    print(output)

    # Disable paging
    output = my_conn.disable_paging()
    print(output)
