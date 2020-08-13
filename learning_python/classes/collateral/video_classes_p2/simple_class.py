import ipdb  # noqa


class NetworkDevice:
    def __init__(self, platform, ip_addr):
        self.platform = platform
        self.ip_addr = ip_addr


# ipdb.set_trace()
rtr1 = NetworkDevice("cisco_ios", "1.1.1.1")
