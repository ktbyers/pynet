
from onepk_helper import NetworkDevice

from onep.routing import Routing,RouteRange,L3UnicastScope,L3UnicastRouteRange,L3UnicastRIBFilter
from onep.routing import L3UnicastRIBFilter
from onep.interfaces import NetworkPrefix


def display_routes(net_element):

    ROUTES_TO_RETURN = 10

    # Create a Routing object
    routing = Routing.get_instance(net_element)

    # IPv4 Unicast routes only
    scope = L3UnicastScope("", L3UnicastScope.AFIType.IPV4, L3UnicastScope.SAFIType.UNICAST, "")

    # Get all routes (limited by ROUTES_TO_RETURN)
    prefix = NetworkPrefix("0.0.0.0", 0)
    range = L3UnicastRouteRange(prefix, RouteRange.RangeType.EQUAL_OR_LARGER, ROUTES_TO_RETURN)

    # Create a blank filter object
    filter = L3UnicastRIBFilter()

    # Get the routes
    route_list = routing.rib.get_route_list(scope, filter, range)

    for route in route_list:
        print route.prefix.address + "/" + str(route.prefix.prefix_length)


if __name__ == "__main__":

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

    rtr1_obj = NetworkDevice(**pynet_rtr1)
    rtr2_obj = NetworkDevice(**pynet_rtr2)

    print "\nPrinting routing table from pynet_rtr1"
    rtr1_obj.establish_session()
    display_routes(rtr1_obj.net_element)
    rtr1_obj.disconnect()

    print "\nPrinting routing table from pynet_rtr2"
    rtr2_obj.establish_session()
    display_routes(rtr2_obj.net_element)
    rtr2_obj.disconnect()

    print
