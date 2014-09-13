'''

Applied Python Course, Class1, Exercise 3b

Note, you will need to update the IP and COMMUNITY_STRING to use this script.

Note, making assumption that ccmHistoryStartupLastChanged gets reset to 0 on 
reload.  This was observed on Cisco881, but do not know how general this 
behavior is.

'''

from snmp_helper import snmp_get_oid, snmp_extract


def determine_run_start_sync_state(run_change_sysuptime, start_save_sysuptime):
    '''
    return True if run/start are in sync
    return False if run/start are out of sync (or can't be determined after 
    reload)

    Three cases:
    1. Normal (no reboot): in sync if start_save_sysuptime >= run_change_sysuptime 

    2. Reboot, but subsequent 'wr mem'
       start_save_sysuptime will be non-zero in this case.  In this case
       eventhough there has been a reboot, you can revert to normal method.

    3. Reboot, and no subsequent 'wr mem'
       start_save_sysuptime = 0 in this case.  You can't determine whether the
       run and start are in sync (using this method).  Return False in this
       case.

    '''

    # No 'wr mem' since last reload
    if start_save_sysuptime == 0:
        return False

    elif start_save_sysuptime >= run_change_sysuptime:
        return True

    return False


def convert_uptime_hours(sys_uptime):
    '''
    sys_uptime is in hundredths of seconds

    returns a float
    '''
    return int(sys_uptime) / 100.0 / 3600.0


def main():
    '''
    '''

    DEBUG = False

    COMMUNITY_STRING = '********'
    IP = '10.10.10.10'
    
    my_devices = {
        "pynet_rtr1": (IP, COMMUNITY_STRING, 7961),
        "pynet_rtr2": (IP, COMMUNITY_STRING, 8061),
    }

    # Uptime when running config last changed
    ccmHistoryRunningLastChanged = '1.3.6.1.4.1.9.9.43.1.1.1.0'
    # Uptime when running config last saved (note any 'write' constitutes a save)
    ccmHistoryRunningLastSaved = '1.3.6.1.4.1.9.9.43.1.1.2.0'
    # Uptime when startup config last saved
    ccmHistoryStartupLastChanged = '1.3.6.1.4.1.9.9.43.1.1.3.0'
    
    sys_uptime_oid = '1.3.6.1.2.1.1.3.0'
    
    
    for device_name, snmp_device in my_devices.items():
   
        # Gather data from device 
        snmp_data = snmp_get_oid(snmp_device, oid=sys_uptime_oid)
        sys_uptime = snmp_extract(snmp_data)
    
        uptime_hours = convert_uptime_hours(sys_uptime)
    
        snmp_data = snmp_get_oid(snmp_device, oid=ccmHistoryRunningLastChanged)
        last_run_change = int(snmp_extract(snmp_data))
    
        snmp_data = snmp_get_oid(snmp_device, oid=ccmHistoryStartupLastChanged)
        last_start_save = int(snmp_extract(snmp_data))

        # Determine whether run-start are in sync    
        run_save_status = determine_run_start_sync_state(last_run_change, last_start_save)

        # Display output
        print "\nDevice = %s" % device_name
        print "Current Uptime = %.1f hours" % uptime_hours
        if DEBUG:
            print "Run change time = %s" % last_run_change
            print "Last save time = %s" % last_start_save

        # Check for a reboot and no save
        if not(last_start_save):
            print 'This device has never been saved since the last reboot'
        else:
            if run_save_status:
                print 'Running config has been saved'
            else:
                print 'Running config not saved'
    
        print


if __name__ == '__main__':

    main()
