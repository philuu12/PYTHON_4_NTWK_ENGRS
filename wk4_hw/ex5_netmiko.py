#!/usr/bin/env python
"""
Assignment 5:
Use Netmiko to enter into configuration mode on pynet-rtr2. Also use Netmiko to verify
your state (i.e. that you are currently in configuration mode).
"""
from netmiko import ConnectHandler
from getpass import getpass
password = getpass()

pynet2 = {
            'device_type': 'cisco_ios',
            'ip': '50.76.53.27',
            'username': 'pyclass',
            'password': password,       # it's 88newclass
            'port': 8022,
        }

pynet_rtr2 = ConnectHandler(**pynet2)

# Enter into the Config mode of pynet-rtr2 router
prompt = pynet_rtr2.find_prompt()
print "Prompt: ", prompt
pynet_rtr2.config_mode()

# Check if you are currently in Config mode. Return True if in Config mode; else False
config_md_status = pynet_rtr2.check_config_mode()
if config_md_status:
    print "Verified: In Config mode status!"
else:
    print "Failed: Not in Config mode status!"


