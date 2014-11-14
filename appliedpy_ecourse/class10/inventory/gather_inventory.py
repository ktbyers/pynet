
class GatherInventory(object):
    '''
    Base class

    Any methods here will be generic or based on Cisco IOS

    Specific vendors will be child classes of this class.
    '''

    def __init__(self, net_device, output):
        self.net_device = net_device
        self.output = output

    def find_vendor(self):
        pass

    def find_model(self):
        pass

    def find_device_type(self):
        pass

    def find_os_version(self):
        pass

    def find_serial_number(self):
        pass

    def find_uptime(self):
        pass

