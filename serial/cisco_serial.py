'''
Testing using Python to interact to Cisco router via serial port
'''

import serial
import sys
import time

import credentials

READ_TIMEOUT = 8


def read_serial(console):
    '''
    Check if there is data waiting to be read

    Read and return it.

    else return null string
    '''
    data_bytes = console.inWaiting()
    if data_bytes:
        return console.read(data_bytes)
    else:
        return ""


def check_logged_in(console):
    '''
    Check if logged in to router
    '''
    console.write("\r\n\r\n")
    time.sleep(1)
    prompt = read_serial(console)
    if '>' in prompt or '#' in prompt:
        return True
    else:
        return False


def login(console):
    '''
    Login to router
    '''
    login_status = check_logged_in(console)
    if login_status:
        print "Already logged in"
        return None

    print "Logging into router"
    while True:
        console.write("\r\n")
        time.sleep(1)
        input_data = read_serial(console)
        if not 'Username' in input_data:
            continue
        console.write(credentials.username + "\r\n")
        time.sleep(1)

        input_data = read_serial(console)
        if not 'Password' in input_data:
            continue
        console.write(credentials.password + "\r\n")
        time.sleep(1)

        login_status = check_logged_in(console)
        if login_status:
            print "We are logged in\n"
            break


def logout(console):
    '''
    Exit from console session
    '''
    print "Logging out from router"
    while check_logged_in(console):
        console.write("exit\r\n")
        time.sleep(.5)

    print "Successfully logged out from router"


def send_command(console, cmd=''):
    '''
    Send a command down the channel

    Return the output
    '''
    console.write(cmd + '\r\n')
    time.sleep(1)
    return read_serial(console)


def main():
    '''
    Testing using Python to interact to Cisco router via serial port
    '''

    print "\nInitializing serial connection"

    console = serial.Serial(
        port='COM1',
        baudrate=9600,
        parity="N",
        stopbits=1,
        bytesize=8,
        timeout=READ_TIMEOUT
    )

    if not console.isOpen():
        sys.exit()

    login(console)
    print send_command(console, cmd='show ip int brief')

    logout(console)


if __name__ == "__main__":
    main()
