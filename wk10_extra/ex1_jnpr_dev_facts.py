#!/usr/bin/env python

# 1. Use Juniper's PyEZ library to make a connection to the Juniper SRX
# and to print out the device's facts.

from jnpr.junos import Device
from getpass import getpass
from pprint import pprint

pwd = getpass() 
a_device = Device(host='50.76.53.27', user='pyclass', password=pwd)
a_device.open()
pprint(a_device.facts)
#Matma: tamtamnewclass
