import re
from gather_inventory import GatherInventory
from general_functions import parse_uptime

class AristaGatherInventory(GatherInventory):


    def find_vendor(self):
        if 'Arista' in self.output:
            self.net_device.vendor = 'arista'
            self.net_device.save()
        else:
            raise ValueError("Invalid vendor")


    def find_model(self):
        '''
        Arista show version first line is the following

        Arista DCS-7124S-F
        '''

        # Get first line of the output
        tmp_output = self.output.strip()
        model = tmp_output.split('\n')[0]

        if 'Arista ' in model:
            self.net_device.model = model.split('Arista ')[1]
            self.net_device.save()
            

    def find_device_type(self):
        if self.net_device.model == 'vEOS':
            self.net_device.device_type = 'switch'
            self.net_device.save()
        else:
            raise ValueError("Unable to find device_type from model({})".format(self.net_device.model))


    def find_os_version(self):
        '''
        String in show version will be similar to the following:
        Software image version: 4.12.1-1356975.vEOS4123 (engineering build)
        '''

        match = re.search(r'Software image version: (.*)', self.output)
        if match:
            self.net_device.os_version = match.group(1)
            self.net_device.save()


    def find_serial_number(self):
        '''
        For vEOS use the MAC address (S/N is blank)

        String in show version will be similar to the following:
        Serial number:       JSH10170315
        '''

        if self.net_device.model == 'vEOS':
            match = re.search(r'System MAC address: +(\w.*)', self.output)
        else:
            match = re.search(r'Serial number: +(\w+)', self.output)

        if match:
            self.net_device.serial_number = match.group(1)
            self.net_device.save()


    def find_uptime(self):
        '''
        String in show version will be similar to the following:
        Uptime:                 5 weeks, 4 days, 23 hours and 8 minutes
        '''

        match = re.search(r'Uptime: +(\w.*)', self.output)
        if match:
            time_str = match.group(1)
            self.net_device.uptime_seconds = parse_uptime(time_str)
            self.net_device.save()


