import paramiko
import time

MAX_BUFFER = 65535


class SSHConnection(object):
    '''
    Base class is based upon Cisco IOS behavior.

    Should subclass this class for different vendors.
    '''

    def __init__(self, net_device):
        self.net_device = net_device
        self.ip = net_device.ip_address
        
        if net_device.ssh_port:
            self.port = net_device.ssh_port
        else:
            self.port = 22

        self.username = net_device.credentials.username
        self.password = net_device.credentials.password

        self.establish_connection()
        self.find_prompt()


    def establish_connection(self):
        '''
        Establish SSH connection to the network device
        '''

        VERBOSE = False

        if VERBOSE:
            print "#" * 80

        # Create instance of SSHClient object
        self.remote_conn_pre = paramiko.SSHClient()

        # Automatically add untrusted hosts (make sure okay for security policy in your environment)
        self.remote_conn_pre.set_missing_host_key_policy(
             paramiko.AutoAddPolicy())

        # initiate SSH connection
        print "SSH connection established to {}:{}".format(self.ip, self.port)
        self.remote_conn_pre.connect(hostname=self.ip, port=self.port, username=self.username, password=self.password)

        # Use invoke_shell to establish an 'interactive session'
        self.remote_conn = self.remote_conn_pre.invoke_shell()
        print "Interactive SSH session established"

        # Strip the initial router prompt
        time.sleep(3)
        output = self.remote_conn.recv(MAX_BUFFER)

        self.disable_paging()

        if VERBOSE:
            print output
            print "#" * 80
            print



    def disable_paging(self):
        '''
        Disable paging on a Cisco router
        '''

        self.remote_conn.send("terminal length 0\n")
        time.sleep(1)

        # Clear the buffer on the screen
        return self.remote_conn.recv(MAX_BUFFER)


    def find_prompt(self):
        """
        Finds the network device name and prompt ('>', '#')
        """
    
        DEBUG = False
        if DEBUG: print "In find_prompt"

        self.remote_conn.send("\n")
        time.sleep(1)

        router_name = self.remote_conn.recv(MAX_BUFFER)

        if (router_name.count('>') == 1):
            z_prompt = '>'
            router_name = router_name.split('>')[0]
        elif (router_name.count('#') == 1):
            z_prompt = '#'
            router_name = router_name.split('#')[0]
        else:
            raise ValueError("Router name not found after multiple attempts")

        router_name = self.normalize_linefeeds(router_name)
        self.router_name = router_name.strip()
        self.router_prompt = self.router_name + z_prompt
        if DEBUG: print "router_name: {}; prompt: {}".format(self.router_name, self.router_prompt)


    def clear_buffer(self):
        '''
        Read any data available in the channel 
        '''

        if self.remote_conn.recv_ready():
            return self.remote_conn.recv(MAX_BUFFER)
        else:
            return None

    
    def send_command(self, command_string, delay_factor=1, max_loops=30):
        """
        Execute command_string on the SSH channel.

        Use delay based mechanism to obtain output.  Strips echoed characters and router prompt.

        delay_factor can be used to increase the delays.

        max_loops can be used to increase the number of times it reads the data buffer
        
        Returns the output of the command.
        """

        DEBUG = False
        output = ''

        if DEBUG: print 'In send_command'

        self.clear_buffer()

        # Ensure there is a newline at the end of the command
        command_string = command_string.rstrip("\n")
        command_string += '\n'

        if DEBUG: print "Command is: {}".format(command_string)
 
        self.remote_conn.send(command_string)

        time.sleep(1*delay_factor)
        not_done = True
        i = 1

        while (not_done) and (i <= max_loops):

            if DEBUG: print "In while loop"
            time.sleep(2*delay_factor)
            i += 1

            # Keep reading data as long as available (up to max_loops)
            if self.remote_conn.recv_ready():
                if DEBUG: print "recv_ready = True"
                output += self.remote_conn.recv(MAX_BUFFER)
            else:
                if DEBUG: print "recv_ready = False"
                not_done = False

        output = self.normalize_linefeeds(output)
        output = self.strip_command(command_string, output)
        output = self.strip_prompt(output)
   
        if DEBUG: print output 
        return output


    def strip_prompt(self, a_string):

        DEBUG = False

        response_list = a_string.split('\n')
        if response_list[-1] == self.router_prompt:
            if DEBUG: print "Stripping router prompt {}".format(response_list[-1])
            return '\n'.join(response_list[:-1])
        else:
            return a_string


    def strip_command(self, command_string, output):
        '''
        Strip command_string from output string
        '''

        command_length = len(command_string)
        return output[command_length:]


    def normalize_linefeeds(self, a_string):
        '''
        Convert '\r\n' to '\n'
        '''

        return a_string.replace('\r\n', '\n')


    def enable_mode(self):
        '''
        Needs expanded to include sending enable secret
        '''
        output = self.send_command('enable\n')
        self.find_prompt()
        self.clear_buffer()

        return output


    def config_mode(self):
        pass
