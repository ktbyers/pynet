
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
        '''
        Generic find_vendor method
        '''
        pass

    def find_model(self):
        '''
        Generic find_model method
        '''
        pass

    def find_device_type(self):
        '''
        Generic find_device_type method
        '''
        pass

    def find_os_version(self):
        '''
        Generic find_os_version method
        '''
        pass

    def find_serial_number(self):
        '''
        Generic find_serial_number method
        '''
        pass

    def find_uptime(self):
        '''
        Generic find_uptime method
        '''
        pass

