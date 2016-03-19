#!/usr/bin/env python
# 2. For each of the SRX's interfaces, display: the operational state, 
# packets-in, and packets-out. You will probably want to use EthPortTable
# for this.

from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable
from pprint import pprint
from getpass import getpass

pwd = getpass()
a_device = Device(host='50.76.53.27', user='pyclass', password=pwd)
a_device.open()     # Establich connection to Juniper SRX device

# Instantiagte an EthPortTable object
ports = EthPortTable(a_device)

# Retrieve data from ports
ports.get()

# Retrieve port numbers and recursively obtain other info from there   
for a_port in ports.keys():
    print ("Port: %s, Operating state: %s, Rx Packets: %s, Tx Packets: %s" 
           % (a_port,
              ports[a_port]['oper'],
              ports[a_port]['rx_packets'],
              ports[a_port]['tx_packets']))
# mm = tamtamnewclass
