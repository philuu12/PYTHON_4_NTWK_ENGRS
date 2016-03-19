#!/usr/bin/env python
"""
3. Display the SRX's routing table. You will probably want to use RouteTable
for this (from jnpr.junos.op.routes import RouteTable).

The output should look similiar to the following:

Juniper SRX Routing Table: 

0.0.0.0/0
  nexthop 10.220.88.1
  age 14582542
  via vlan.0
  protocol Static

10.220.88.0/24
  nexthop None
  age 14583120
  via vlan.0
  protocol Direct

10.220.88.39/32
  nexthop None
  age 14583289
  via vlan.0
  protocol Local
"""

from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from getpass import getpass

pwd = getpass() 
a_device = Device(host="50.76.53.27", user='pyclass', password=pwd)

# Establish connection with device
a_device.open()

# Instantiate an RouteTable object
ports = RouteTable(a_device)


# Retrieve data from instantiated object
ports.get()

for a_route in ports.keys():
    print ("%s\n\t%s\n\t%s\n\t%s\n\t%s\n") % \
          (a_route,
           ports[a_route]['nexthop'],
           ports[a_route]['age'],
           ports[a_route]['via'],
           ports[a_route]['protocol']
          )

# mm = tamtamnewclass
