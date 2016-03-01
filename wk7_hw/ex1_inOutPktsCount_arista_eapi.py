#!/usr/bin/env python
"""
1. Use Arista's eAPI to obtain 'show interfaces' from the switch. Parse the 'show interfaces' output to obtain the 'inOctets' and 'outOctets' fields for each of the interfaces on the switch.  Accomplish this using Arista's pyeapi.
"""
import pyeapi 

# Connect a Connection to Arista switch; using the switch specified in
# /home/pluu/.eapi.conf file
# cat .eapi.conf
# ----------------
# (venv)[pluu@ip-172-30-0-57 ~]$ cat .eapi.conf
# [connection:pynet-sw3]
# username: eapi
# password: ZZteslaX
# host: 50.76.53.27
# port: 8443
# transport: https
# (venv)[pluu@ip-172-30-0-57 ~]$
pynet_sw3 = pyeapi.connect_to("pynet-sw3")

gen_res = pynet_sw3.enable("show interfaces")
result_res = gen_res[0]['result']
interface_res    = result_res['interfaces']  

final_stat_dict = {}
for interface, interface_val in interface_res.items():
    # Extract value first
    intf_counters_dict = interface_val.get('interfaceCounters', {}) 

    # Extract final statistics: put both inOctets and outOctets in a set ()
    final_stat_dict[interface] = \
        (intf_counters_dict.get('inOctets'), intf_counters_dict.get('outOctets'))


# Print output data
print "\n{:20} {:<20} {:<20}".format("Interface:", "inOctets", "outOctets")
for intf, octets in final_stat_dict.items():
    print "{:20} {:<20} {:<20}".format(intf, octets[0], octets[1])

print

