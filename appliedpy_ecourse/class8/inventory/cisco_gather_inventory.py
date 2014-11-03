import re
from general_functions import parse_uptime
from gather_inventory import GatherInventory

class CiscoGatherInventory(GatherInventory):
    '''
    Based-on Cisco IOS
    '''

    def find_vendor(self):
        if 'Cisco' in self.output:
            self.net_device.vendor = 'cisco'
            self.net_device.save()
        else:
            raise ValueError("Invalid vendor")


    def find_model(self):
        match = re.search(r'.*bytes of memory', self.output) 
        if match:
            model = match.group()
            self.net_device.model = model.split()[1]
            self.net_device.save()
            

    def find_device_type(self):
        if self.net_device.model == '881':
            self.net_device.device_type = 'router'
        else:
            raise ValueError("Unable to find device_type from model({})".format(self.net_device.model))

        self.net_device.save()


    def find_os_version(self):
        '''
        String in show version will be similar to the following:
        Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.4(2)T1, RELEASE SOFTWARE (fc3)
        '''

        match = re.search(r'Cisco IOS Software, (.*)', self.output)
        if match:
            self.net_device.os_version = match.group(1)
            self.net_device.save()


    def find_serial_number(self):
        '''
        String in show version will be similar to the following:
        Processor board ID FTX10000001
        '''

        match = re.search(r'Processor board ID (.*)', self.output)
        if match:
            self.net_device.serial_number = match.group(1)
            self.net_device.save()


    def find_uptime(self):
        '''
        String in show version will be similar to the following:
        hostname uptime is 8 weeks, 2 days, 23 hours, 22 minutes
        '''

        match = re.search(r'uptime is (.*)', self.output)
        if match:
            time_str = match.group(1)
            self.net_device.uptime_seconds = parse_uptime(time_str)
