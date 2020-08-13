import ipdb  # noqa


class NetworkDevice:
    def __init__(self, platform, ip_addr):
        self.platform = platform
        self.ip_addr = ip_addr

    def say_hello(self):
        print("Hello")

    def say_ip(self):
        print(f"IP Addr: {self.ip_addr}")

    def say_platform(self):
        print(f"Platform: {self.platform}")


# ipdb.set_trace()
rtr1 = NetworkDevice("cisco_ios", "1.1.1.1")
rtr1.say_hello()
rtr1.say_ip()
rtr1.say_platform()
