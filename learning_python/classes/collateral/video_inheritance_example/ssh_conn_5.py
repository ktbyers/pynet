from getpass import getpass
import ipdb
import paramiko
import time


class NetworkDevice:
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
        self.remote_conn_pre = remote_conn_pre
        self.remote_conn = remote_conn_pre.invoke_shell()

    def send(self, data):
        self.remote_conn.send(data)

    def recv(self):
        max_buffer = 65535
        in_data = ""
        if self.remote_conn.recv_ready():
            in_data = self.remote_conn.recv(max_buffer)
            in_data = in_data.decode()
        return in_data

    def say_hello(self):
        print("Hello world")


class CiscoIosXE(NetworkDevice):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.platform = "cisco_xe"

    def setup(self):
        self.send("terminal width 512\n")
        self.send("terminal length 0\n")
        time.sleep(0.5)
        output = self.recv()
        print(output)


class JuniperJunos(NetworkDevice):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.platform = "juniper_junos"

    def setup(self):
        self.send("set cli screen-width 511\n")
        self.send("set cli screen-length 0\n")
        time.sleep(0.5)
        output = self.recv()
        print(output)

    def say_hello(self):
        print(f"Hello...my platform is {self.platform}")


if __name__ == "__main__":

    ipdb.set_trace()
    password = getpass()
    cisco6 = {
        "host": "cisco6.lasthop.io",
        "username": "pyclass",
        "password": password,
    }

    vmx2 = {
        "host": "vmx2.lasthop.io",
        "username": "pyclass",
        "password": password,
    }

    conn1 = CiscoIosXE(**cisco6)
    conn1.open()
    conn1.setup()

    conn2 = JuniperJunos(**vmx2)
    conn2.open()
    conn2.setup()
    ipdb.set_trace()
    print(conn2)
