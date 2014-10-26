'''
Using onePK and the VTY Service obtain the output from the 'show version' 
command.  Use 'terminal length 0' to disable output paging (i.e. disable 
'--More--' prompting).

'''

from onepk_helper import NetworkDevice
from onep.vty import VtyService


def main():

    pynet_rtr1 = dict(
        ip = '10.10.10.10',
        username = 'pyclass',
        password = '********',
        pin_file = 'pynet-rtr1-pin.txt',
        port = 15002
    )

    pynet_rtr2 = dict(
        ip = '10.10.10.10',
        username = 'pyclass',
        password = '********',
        pin_file = 'pynet-rtr2-pin.txt',
        port = 8002
    )

    for a_rtr in (pynet_rtr1, pynet_rtr2):

        rtr_obj = NetworkDevice(**a_rtr)
        rtr_obj.establish_session()

        rtr_name = rtr_obj.net_element.properties.sys_name

        vty_service = VtyService(rtr_obj.net_element)
        vty_service.open()

        CMD = "terminal length 0"
        cli = vty_service.write(CMD)
        CMD = "show version"
        cli = vty_service.write(CMD)

        print "\n" + "*" * 80
        print "** CONNECTED TO: {}".format(rtr_name)
        print "*" * 80
        print cli
        print "*" * 80
        print "\n\n"

        rtr_obj.disconnect()


if __name__ == "__main__":

    main()

