#!/usr/bin/env python
"""
Assignment 7:
Use Netmiko to change the logging buffer size (logging buffered <size>) on pynet-rtr2.
"""
import re
from netmiko import ConnectHandler
from getpass import getpass
password = getpass()

pynet2 = {
            'device_type': 'cisco_ios',
            'ip': '50.76.53.27',
            'username': 'pyclass',
            'password': password,
            'port': 8022,
        }
# Connect to Cisco Router 2
pynet_rtr2 = ConnectHandler(**pynet2)

# Enter Config mode
pynet_rtr2.config_mode()

if (pynet_rtr2.check_config_mode()):
    outp = pynet_rtr2.send_command('logging buffered 25000')
   
    # Exit Config mode 
    pynet_rtr2.exit_config_mode()    

    # Obtain the running Config
    outp = pynet_rtr2.send_command('show runn | inc logging buffered 25000')

    if re.search(r'logging buffered 25000', outp):
        print "Config changed successfully!"
    else:
        print "Config changed unsuccessfully!"
else:
    print "Failed to enter Config mode!"
    
