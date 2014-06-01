'''
Obtain the OS version from the show version output

Example from Cisco IOS
'Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4,
RELEASE SOFTWARE (fc1)'

'''

import re

def obtain_os_version(show_ver):

    # (.+?), means any sequence of one or more characters followed by comma (shortest match)
    match = re.search(r"Cisco IOS Software.*Version (.+?),", show_ver)
    if match:
        return match.group(1)
    else:
        return None


if __name__ == "__main__":

    f = open("../show_version.txt")

    show_ver = f.read()

    print obtain_os_version(show_ver)

