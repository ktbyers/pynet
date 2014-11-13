pynet
=====

Python for Network Engineers

https://pynet.twb-tech.com


Classes 7 - 10 are part of building a larger system 

This is the finished system. 

It does the following:  
1)Inventory collection using onePK, eAPI, and SSH.  
2)Uses SNMP configuration change detection to determine if the configuration
  has changed (currently Cisco only).  
3)Archive the device configuration if is new or has changed (Cisco only).  
4)Send email notification for configuration changes including differences.  
5)Sync configurations into Git.  


To do:  
1)Add Arista support for SNMPv3 and for SNMP configuration change detection.  
2)Archive configurations using onePK and eAPI (if possible).  

