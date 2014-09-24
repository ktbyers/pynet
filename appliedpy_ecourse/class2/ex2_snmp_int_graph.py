'''
https://pynet.twb-tech.com
Applied Python, Class2, Exercise2

Note, you will need to update the IP, SNMP username and keys to use this script.

'''

from snmp_helper import snmp_get_oid_v3,snmp_extract
import line_graph
import time 


def get_interface_stats(snmp_device, snmp_user, stat_type, row_number):
    '''
    stat_type can be 'in_octets, out_octets, in_ucast_pkts, out_ucast_pkts

    returns the counter value as an integer
    '''

    oid_dict = {
        'in_octets':    '1.3.6.1.2.1.2.2.1.10',
        'out_octets':   '1.3.6.1.2.1.2.2.1.16',
        'in_ucast_pkts':    '1.3.6.1.2.1.2.2.1.11',
        'out_ucast_pkts':    '1.3.6.1.2.1.2.2.1.17',
    }

    if not stat_type in oid_dict.keys():
        raise ValueError("Invalid value for stat_type: {}" % stat_type)

    # Make sure row_number can be converted to an int
    row_number = int(row_number)

    # Append row number to OID
    oid = oid_dict[stat_type]
    oid = oid + '.' + str(row_number)

    snmp_data = snmp_get_oid_v3(snmp_device, snmp_user, oid)
    return int(snmp_extract(snmp_data))


def main():
    '''
    Connect to router via SNMPv3.

    Create two graphs in/out octets and in/out packets
    '''

    DEBUG = False

    IP = '1.1.1.1'
    
    a_user = 'someuser'
    auth_key = '*********'
    encrypt_key = '*************'
    
    snmp_user = (a_user, auth_key, encrypt_key)
    
    pynet_rtr1 = (IP, 7961)
    pynet_rtr2 = (IP, 8061)
    snmp_device = pynet_rtr1 
    
    # Fa4 is in row number5 in the MIB-2 interfaces table
    row_number = 5

    graph_stats = {
        "in_octets": [],
        "out_octets": [],
        "in_ucast_pkts": [],
        "out_ucast_pkts": [],
    }
    base_count_dict = {}

    # Enter a loop gathering SNMP data every 5 minutes for an hour. 
    for time_track in range(0,65,5):
    
        print "\n%20s %-60s" % ("time", time_track)

        # Gather SNMP statistics for these four fields
        for entry in ("in_octets", "out_octets", "in_ucast_pkts", "out_ucast_pkts"):

            # Retrieve the SNMP data
            snmp_retrieved_count = get_interface_stats(snmp_device, snmp_user, entry, row_number)

            # Get the base counter value 
            base_count = base_count_dict.get(entry)
            if base_count:
                # Save the data to graph_stats dictionary
                graph_stats[entry].append(snmp_retrieved_count - base_count)
                print "%20s %-60s" % (entry, graph_stats[entry][-1])

            # Update the base counter value
            base_count_dict[entry] = snmp_retrieved_count

        time.sleep(300)


    print
    if DEBUG: print graph_stats

    x_labels = []
    for x in range(5,65, 5):
        x_labels.append(str(x))

    if DEBUG: print x_labels


    # Create the graphs
    if line_graph.twoline("pynet-rtr1-octets.svg", "pynet-rtr1 Fa4 Input/Output Bytes", graph_stats["in_octets"], 
                "In Octets", graph_stats["out_octets"], "Out Octets", x_labels):
        print "In/Out Octets graph created"

    if line_graph.twoline("pynet-rtr1-pkts.svg", "pynet-rtr1 Fa4 Input/Output Unicast Packets", graph_stats["in_ucast_pkts"], 
                "In Packets", graph_stats["out_ucast_pkts"], "Out Packets", x_labels):
        print "In/Out Packets graph created"

    print


if __name__ == '__main__':
    main() 
