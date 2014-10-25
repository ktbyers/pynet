'''
Using the onepk_helper library establish a onePK connection to one of the two 
lab routers.  From this lab router obtain the product_id and SerialNo:

>>> rtr_obj.net_element.properties.product_id
'CISCO881-SEC-K9'
>>> rtr_obj.net_element.properties.SerialNo
'FTX1000008X'

'''

from onepk_helper import NetworkDevice


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
        
        print "\nConnection established to: {}".format(rtr_obj.net_element.properties.sys_name)
        print rtr_obj.net_element.properties.product_id
        print rtr_obj.net_element.properties.SerialNo

        rtr_obj.disconnect()

    print


if __name__ == "__main__":

    main()

