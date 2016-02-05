#!/usr/bin/env python
"""
Problem 1. Using SNMPv3 create a script that detects router configuration changes.
[1. done] If the running configuration has changed, then send an email notification to yourself identifying 
the router that changed and the time that it changed.
Note, the running configuration of pynet-rtr2 is changing every 15 minutes (roughly at 0, 15, 30, and 45 minutes after the hour).
This will allow you to test your script in the lab environment. 

[2. done] In this exercise, you will possibly need to save data to an external file.
One way you can accomplish this is by using a pickle file, see:  
    http://youtu.be/ZJOJjyhhEvM  
A pickle file lets you save native Python data structures (dictionaries, lists, objects) directly to a file.

[3. done] Here is some additional reference material that you will probably need to solve this problem:
Cisco routers have the following three OIDs:
# Uptime when running config last changed
ccmHistoryRunningLastChanged = '1.3.6.1.4.1.9.9.43.1.1.1.0'   

# Uptime when running config last saved (note any 'write' constitutes a save)    
ccmHistoryRunningLastSaved = '1.3.6.1.4.1.9.9.43.1.1.2.0'   

# Uptime when startup config last saved   
ccmHistoryStartupLastChanged = '1.3.6.1.4.1.9.9.43.1.1.3.0'

From the above descriptions, the router will save 1) the sysUptime timestamp (OID sysUptime = 1.3.6.1.2.1.1.3.0) 
when a running configuration change occurs. The router will also record the 2) sysUptime timestamp when 
the running configuration is saved to the startup config.

Here is some data on the behavior of these OIDs. Note, sysUptime times are in hundredths of seconds
so 317579 equals 3175.79 seconds (i.e. a bit less than one hour)

# After reboot
pynet-rtr2.twb-tech.com
317579        (sysUptime)
2440          (ccmHistoryRunningLastChanged--running-config is changed during boot)
0             (ccmHistoryRunningLastSaved -- i.e. reset to 0 on reload)
0             (ccmHistoryStartupLastChanged -- i.e. reset to 0 on reload)

# After config change on router (but no save to startup config)
pynet-rtr2.twb-tech.com
322522        (sysUptime)
322219        (ccmHistoryRunningLastChanged)
0             (ccmHistoryRunningLastSaved)
0             (ccmHistoryStartupLastChanged)

# After 'write mem' on router
pynet-rtr2.twb-tech.com
324543        (sysUptime)
322219        (ccmHistoryRunningLastChanged)
323912        (ccmHistoryRunningLastSaved)
323912        (ccmHistoryStartupLastChanged)

# After another configuration change (but no save to startup config)
pynet-rtr2.twb-tech.com
327177        (sysUptime)
326813        (ccmHistoryRunningLastChanged)
323912        (ccmHistoryRunningLastSaved)
323912        (ccmHistoryStartupLastChanged)

# After 'show run' command (note, this causes 'ccmHistoryRunningLastSaved' to 
# increase i.e. 'write terminal' causes this OID to be updated)
pynet-rtr2.twb-tech.com
343223        (sysUptime)
326813        (ccmHistoryRunningLastChanged)
342898        (ccmHistoryRunningLastSaved)
323912        (ccmHistoryStartupLastChanged)

Bonus challenge: instead of saving your data in a pickle file, save the data using either a YAML or a JSON file. 
My alternate solution supports pickle, YAML, or JSON depending on the name of the file (.pkl, .yml, or .json).
"""
import time
import json
import snmp_helper
from email_helper import send_mail

IP = '50.76.53.27'
a_user = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'
snmp_user = (a_user, auth_key, encrypt_key)
pynet_rtr2 = (IP, 8061)
SLEEP_TIME = 15
ONE_HOUR = 3600 + 5         # Add 5 seconds, so last time stamp change executed
recipient = 'philuu12@gmail.com'
sender = 'philuu12@gmail.com'
subject = 'Running config changes'

# Begin -- Figure out the System name
snmp_sys_name = snmp_helper.snmp_get_oid_v3(pynet_rtr2, snmp_user, oid='1.3.6.1.2.1.1.5.0')
sys_name = snmp_helper.snmp_extract(snmp_sys_name)
print "Router name is: ", sys_name
# End -- Figure out the System name

start_time = time.time()
elapsed_time = 0

# Previous running-config time stamp
prev_run_cfg_chg_stmp = 0

while (elapsed_time <= ONE_HOUR):
    # Debounce the data being read by sleeping 15 seconds to let data stabilized
    print "Sleeping for {} seconds before sampling data again ...".format(SLEEP_TIME)
    time.sleep(SLEEP_TIME)

    # ccmHistoryRunningLastChanged = '1.3.6.1.4.1.9.9.43.1.1.1.0'   
    # (aka, time stamp of ccmHistoryRunningLastChanged)
    # Get the current value of OID '1.3.6.1.4.1.9.9.43.1.1.1.0'
    # (which is a time stamp of RunningLastChanged)
    snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr2, snmp_user, oid='1.3.6.1.4.1.9.9.43.1.1.1.0')
    # Convert the current value of OID 1.3.6.1.4.1.9.9.43.1.1.1.0
    # into a human-readable time-stamp string
    output = snmp_helper.snmp_extract(snmp_data)
    print "SNMP Data Output: ", output

    # Timestamnp of RunningLastChanged
    cur_run_cfg_chg_stmp = output

    # Running-config file of Router py_rtr2 configured to update every 15 minutes 
    if (cur_run_cfg_chg_stmp > prev_run_cfg_chg_stmp):
        prev_run_cfg_chg_stmp = cur_run_cfg_chg_stmp
        print "Change occurs!"
        message = """
        There are changes in running config.
        Router IP address: {router_ip}
        Router Name: {router_name}
        Change time: {change_time}
        Regards,

        Phi
        """.format(router_ip=pynet_rtr2, router_name=sys_name, change_time=cur_run_cfg_chg_stmp)
        send_mail(recipient, subject, message, sender)

        with open("run_cfg_last_stmp.json", "a") as f:
            json.dump("Saving Last changed time of Running configuration\n", f)
            json.dump("Router: {router}".format(router=pynet_rtr2), f)
            json.dump("Last change time: {change_time}".format(change_time=cur_run_cfg_chg_stmp), f)
            json.dump("=================================================\n", f)

    elapsed_time = time.time() - start_time
    
f.close()


