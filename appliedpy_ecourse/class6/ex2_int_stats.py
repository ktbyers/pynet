'''
Print out the interface statistics for FastEthernet4 on the two lab routers 
(rtr1 = port 15002, rtr2 = port 8002).

'''

from onepk_helper import NetworkDevice
from onep.interfaces import NetworkInterface,InterfaceFilter


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

        # Create a filter for only Enet interfaces
        filter = InterfaceFilter(None,NetworkInterface.InterfaceTypes.ONEP_IF_TYPE_ETHERNET)

        # Get the interfaces
        int_list = rtr_obj.net_element.get_interface_list(filter)

        print 
        for intf in int_list:
            if 'FastEthernet4' in intf.name:
                rtr_name = rtr_obj.net_element.properties.sys_name
                print "{} ({}) interface statistics:".format(rtr_name, intf.name)
                print intf.get_statistics()

        rtr_obj.disconnect()

    print


if __name__ == "__main__":

    main()

