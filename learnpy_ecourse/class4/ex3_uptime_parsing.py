#!/usr/bin/env python

'''

Disclaimer - This is a solution to the below problem given the content we have
discussed in class.  It is not necessarily the best solution to the problem.
In other words, I generally only use things we have covered up to this point
in the class (with some exceptions which I will usually note). 

Python for Network Engineers
https://pynet.twb-tech.com
Learning Python


Create a program that converts the following uptime strings to a time in 
seconds.

uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

For each of these strings store the uptime in a dictionary using the device name
as the key.

During this conversion process, you will have to convert strings to integers.
For these string to integer conversions use try/except to catch any string to
integer conversion exceptions.

For example:
int('5') works fine
int('5 years') generates a ValueError exception.

Print the dictionary to standard output.

'''

import pprint

DEBUG = False

# Easier to store these as constants
MINUTE_SECONDS = 60
HOUR_SECONDS = 60 * MINUTE_SECONDS
DAY_SECONDS = 24 * HOUR_SECONDS
WEEK_SECONDS = 7 * DAY_SECONDS
YEAR_SECONDS = 365 * DAY_SECONDS


uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

uptime_dict = {}
uptime_dict2 = {}

for uptime in (uptime1, uptime2, uptime3, uptime4):

    uptime_fields = uptime.split(',')

    # Extract the hostname from uptime_fields
    (hostname, time_field1) = uptime_fields[0].split(' uptime is ')
    uptime_fields[0] = time_field1

    if DEBUG:
        print hostname
        print uptime_fields


    # Two solutions - solution1: long but easier to read
    uptime_seconds = 0
    for time_field in uptime_fields:

        if 'year' in time_field:
            (years, junk) = time_field.split(' year')
            try:
                uptime_seconds += int(years) * YEAR_SECONDS
            except ValueError:
                print "Error, during string conversion to integer"

        elif 'week' in time_field:
            (weeks, junk) = time_field.split(' week')
            try:
                uptime_seconds += int(weeks) * WEEK_SECONDS
            except ValueError:
                print "Error, during string conversion to integer"

        elif 'day' in time_field:
            (days, junk) = time_field.split(' day')
            try:
                uptime_seconds += int(days) * DAY_SECONDS
            except ValueError:
                print "Error, during string conversion to integer"
        
        elif 'hour' in time_field:
            (hours, junk) = time_field.split(' hour')
            try:
                uptime_seconds += int(hours) * HOUR_SECONDS
            except ValueError:
                print "Error, during string conversion to integer"

        elif 'minute' in time_field:
            (minutes, junk) = time_field.split(' minute')
            try:
                uptime_seconds += int(minutes) * MINUTE_SECONDS
            except ValueError:
                print "Error, during string conversion to integer"

    uptime_dict[hostname] = uptime_seconds


    # Two solutions - solution2: the pattern in solution1 is repeated multiple
    # times (use a for loop instead)
    uptime_seconds2 = 0
    for time_field in uptime_fields:
        for string_pattern, time_factor in ( (' year', YEAR_SECONDS),  
                                             (' week', WEEK_SECONDS), 
                                             (' day', DAY_SECONDS), 
                                             (' hour', HOUR_SECONDS), 
                                             (' minute', MINUTE_SECONDS) ):
            if string_pattern in time_field:
                (the_time, junk) = time_field.split(string_pattern)
                try:
                    uptime_seconds2 += int(the_time) * time_factor
                except ValueError:
                    print "Error, during string conversion to integer"

    uptime_dict2[hostname] = uptime_seconds2



# Do the final printing to standard output
print "\nMethod1:"
pprint.pprint(uptime_dict)
print "\nMethod2:"
pprint.pprint(uptime_dict2)
print

