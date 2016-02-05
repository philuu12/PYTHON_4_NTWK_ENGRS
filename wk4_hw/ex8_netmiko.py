#!/usr/bin/env python
"""
Assignment 8:
Use Netmiko to change the logging buffer size (logging buffered <size>) and
to disable console logging (no logging console) from a file on both
pynet-rtr1 and pynet-rtr2 (see 'Errata and Other Info, item #4).

Item 4: Netmiko supports a method (send_config_from_file) that allows you to 
execute configuration commands directly from a file. For example, if you had 
a set of commands in a file called 'config_file.txt', then you could execute
those commands via the SSH channel as follows:
    net_connect.send_config_from_file(config_file='config_file.txt')
"""
from netmiko import ConnectHandler
from getpass import getpass
password = getpass()        # It's 88newclass

pynet1 = {
            'device_type': 'cisco_ios',
            'ip': '50.76.53.27',
            'username': 'pyclass',
            'password': password,
            'port': 22,
        }

pynet2 = {
            'device_type': 'cisco_ios',
            'ip': '50.76.53.27',
            'username': 'pyclass',
            'password': password,
            'port': 8022,
        }

# Enter the Config mode
pynet_rtr1 = ConnectHandler(**pynet1)
pynet_rtr2 = ConnectHandler(**pynet2)

# Configure routers using the Configuration file 'assigned8_conf_file.txt'
pynet_rtr1.config_mode()
pynet_rtr1.send_config_from_file(config_file='ex8_config_file.txt')
pynet_rtr2.config_mode()
pynet_rtr2.send_config_from_file(config_file='ex8_config_file.txt')

# Verify the output
outp = pynet_rtr1.send_command("show running-config")
print "\nOutput of 'show running' for {}:\n{}".format(pynet1['ip'], outp)
outp = pynet_rtr2.send_command("show running-config")
print "\nOutput of 'show running' for {}:\n{}".format(pynet2['ip'], outp)

# Restore the original setting
outp = pynet_rtr1.send_command("logging buffered 20000")
outp = pynet_rtr2.send_command("logging buffered 20000")


