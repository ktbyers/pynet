'''
Obtain the model from the show version output

Example from Cisco IOS:
'Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.'

Returns '881'

'''

import re

def obtain_model(show_ver):
    '''
    Function that processes show version information to obtain the model.
    '''

    # '(.+?) ' means any sequence of one or more characters followed by space (shortest match)
    match = re.search(r"Cisco (.+?) .+bytes of memory", show_ver)
    if match:
        return match.group(1)
    else:
        return None


def main():
    '''
    Obtain the model from the show version output.
    '''

    with open("../show_version.txt") as show_ver_file:
        show_ver = show_ver_file.read()

    print obtain_model(show_ver)


if __name__ == "__main__":
    main()
