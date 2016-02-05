#!/usr/bin/env python
"""
Assignmet 6:
Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx.
"""
from netmiko import ConnectHandler
from getpass import getpass
password = getpass()

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

juniper_srx = {
        'device_type': 'juniper',
        'ip' : '50.76.53.27',
        'username': 'pyclass',
        'password': password,
        'secret': '',
        'port': 9822,
    }

# Connect to routers
pynet_rtr1 = ConnectHandler(**pynet1)
pynet_rtr2 = ConnectHandler(**pynet2)
srx = ConnectHandler(**juniper_srx)

# print out 'show arp' on pynet1
outp1 = pynet_rtr1.send_command("show arp")
print "\n'show arp' of {}:\n{}".format(pynet1['ip'], outp1)

# print out 'show arp' on pynet2
outp2 = pynet_rtr2.send_command("show arp")
print "\n'show arp' of {}:\n{}".format(pynet2['ip'], outp2)

# print out 'show arp' on srx 
outp3 = srx.send_command("show arp")
print "\n'show arp' of {}:{}".format(juniper_srx['ip'], outp3)

