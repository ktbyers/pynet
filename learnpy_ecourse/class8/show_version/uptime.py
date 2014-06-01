'''
Obtain the uptime from the show version output

Example from Cisco IOS:
'twb-sf-881 uptime is 12 weeks, 5 days, 1 hour, 4 minutes'

Returns '12 weeks, 5 days, 1 hour, 4 minutes'

'''

import re

def obtain_uptime(show_ver):

    # '(.+) ' means any sequence of one or more characters to the end of the line
    match = re.search(r".*uptime is (.+)", show_ver)
    if match:
        return match.group(1)
    else:
        return None


if __name__ == "__main__":

    f = open("../show_version.txt")

    show_ver = f.read()

    print obtain_uptime(show_ver)

