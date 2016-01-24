#!/usr/bin/env python

import telnetlib
import time
import sys

TELNET_PORT = 22
TELNET_TIMEOUT = 6
ip_addr = "50.76.53.27"    # pynet-rtr1 hostname
username = "pyclass"
password = "88newclass"

remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)

# Write username
remote_conn.read_until('sername', TELNET_TIMEOUT)
remote_conn.write(username + '\n')

# Write password
remote_conn.read_until('ssword', TELNET_TIMEOUT)
#remote_conn.write(password + '\n')
#time.sleep(1)
# output = remote_conn.read_very_eager()

# Write 'show ip int brief' to router
#remote_conn.write('show ip int brief')
#time.sleep(1)
#output = remote_conn.read_very_eager()
#print output

#remote_conn.close()

