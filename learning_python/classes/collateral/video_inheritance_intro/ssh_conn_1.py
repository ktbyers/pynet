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


class CiscoIosXE(NetworkDevice):
    def setup(self):
        ipdb.set_trace()
        self.send("terminal width 512\n")
        self.send("terminal length 0\n")
        output = self.recv()
        return output


if __name__ == "__main__":

    ipdb.set_trace()
    password = getpass()
    # rtr1 = NetworkDevice(host="cisco6.lasthop.io", username="pyclass", password=password)
    rtr1 = CiscoIosXE(host="cisco6.lasthop.io", username="pyclass", password=password)
    rtr1.open()
    rtr1.setup()
    rtr1.send("\n")
    time.sleep(0.5)
    out = rtr1.recv()
    print(out)
