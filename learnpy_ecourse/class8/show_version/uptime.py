'''
Obtain the uptime from the show version output

Example from Cisco IOS:
'twb-sf-881 uptime is 12 weeks, 5 days, 1 hour, 4 minutes'

Prints to STDOUT '12 weeks, 5 days, 1 hour, 4 minutes'

'''

import re

def obtain_uptime(show_ver):
    '''
    Obtain uptime string from show version output
    '''

    # '(.+) ' means any sequence of one or more characters to the end of the line
    match = re.search(r".*uptime is (.+)", show_ver)
    if match:
        return match.group(1)
    else:
        return None


def main():
    '''
    Obtain the uptime from the show version output

    Prints to STDOUT '12 weeks, 5 days, 1 hour, 4 minutes'
    '''
    with open("../show_version.txt") as show_ver_file:
        show_ver = show_ver_file.read()

    print obtain_uptime(show_ver)


if __name__ == "__main__":
    main()
