'''

Assumes that you have onePK Python SDK installed.
Tested using onePK-sdk-python-rel-1.3.0.181

Assumes that you have previously created pin_file.txt using:
./BaseTutorial.py -a 10.10.10.10 -P pin_file.txt


Example usage:

# Create NetworkDevice object
>>> pynet_rtr1 = dict(
...         ip = '10.10.10.10',
...         username = 'username',
...         password = '********',
...         pin_file = 'pin_file.txt',
...         port = 15002
...     )
>>> rtr1_obj = NetworkDevice(**pynet_rtr1)

# Establish onePK connection
>>> rtr1_obj.establish_session()

# Do something with the session
>>> rtr1_obj.net_element.properties.sys_descr
'Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.4(2)T1, RELEASE SOFTWARE (fc3)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2014 by Cisco Systems, Inc.\nCompiled Thu 26-Jun-14 14:15 by prod_rel_team'

# Disconnect
>>> rtr1_obj.disconnect()

'''

from onep.element.NetworkApplication import NetworkApplication
from onep.element import SessionConfig


class NetworkDevice(object):

    def __init__(self, ip, username, password, pin_file=None, port=15002):
        self.ip = ip
        self.username = username
        self.password = password
        self.pin_file = pin_file
        self.port = port


    def establish_session(self):
        '''
        Take a onepk network device and go through the steps to establish a
        session.
    
        This method assumes that you are using a PIN_FILE

        Sets the following attributes
        self.network_application
        self.net_element
        self.session_config
        self.session_handle
    
        '''
    
        # Create NetworkApplication instance
        self.network_application = NetworkApplication.get_instance()
    
        # Create NetworkElement instance
        self.net_element = self.network_application.get_network_element(self.ip)
    
        # Create SessionConfig instance
        session_config = SessionConfig(SessionConfig.SessionTransportMode.TLS)
        session_config.ca_certs = None
        session_config.keyfile = None
        session_config.certfile = None
        session_config.port = self.port
    
        # Use existing pin_file (previously saved) so that remote certificate is accepted.
        session_config.set_tls_pinning(self.pin_file, None)
        self.session_config = session_config
    
        # Create a session handle object
        self.session_handle = self.net_element.connect(self.username, self.password, self.session_config)


    def disconnect(self):
        '''
        python will hang if you don't gracefully disconnect
        '''

        self.net_element.disconnect()


