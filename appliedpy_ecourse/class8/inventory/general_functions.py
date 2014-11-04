import re

def parse_uptime(time_str):
    '''
    Extract the uptime string from the given device.

    Supports:
        Cisco IOS
        Arista (very limited testing)

    Return the uptime in second; else null string
    '''

    DEBUG = False

    years = weeks = days = hours = minutes = 0
    uptime_sec = 0
    time_list = []
    valid_string = False

    time_str = time_str.strip()
    # Arista uses 'and' in their time string
    time_str = time_str.replace(' and', ',')

    time_list = time_str.split(',')
    if DEBUG: print time_list

    for element in time_list:
        try:
            if ( re.search("year", element)):
                years = int(element.split()[0])
                valid_string = True
            elif ( re.search("week", element)):
                weeks = int(element.split()[0])
                valid_string = True
            elif ( re.search("day", element)):
                days = int(element.split()[0])
                valid_string = True
            elif ( re.search("hour", element)):
                hours = int(element.split()[0])
                valid_string = True
            elif ( re.search("minute", element)):
                minutes = int(element.split()[0])
                valid_string = True
        except (IndexError, ValueError) as e:
            log.exception("Invalid uptime string returned from remote device (%s)" % time_str)
            return ""

    if valid_string:
        uptime_sec = uptime_seconds([years, weeks, days, hours, minutes])
        if DEBUG: print "%s years, %s weeks, %s days, %s hours, %s minutes" % (years, weeks, days, hours, minutes)
        if DEBUG: print "Uptime in minutes = %s" % (uptime_sec)
    else:
        return ""

    return uptime_sec


def uptime_seconds(uptime_list):
    """
    Convert a list of the following form:
    [years, weeks, days, hours, minutes]

    To an uptime in seconds

    """

    years = uptime_list[0]
    weeks = uptime_list[1]
    days = uptime_list[2]
    hours = uptime_list[3]
    minutes = uptime_list[4]

    # No leap day calculation
    days = years*365 + weeks*7 + days
    minutes = days*24*60 + hours*60 + minutes
    seconds = minutes*60

    return seconds

