#!/usr/bin/env python
"""
a. Write a script that connects using telnet to the pynet-rtr1 router. Execute the 'show ip int brief' command on the router and return the output.

Try to do this on your own (i.e. do not copy what I did previously). You should be able to do this by using the following items:

telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
remote_conn.read_until(<string_pattern>, TELNET_TIMEOUT)
remote_conn.read_very_eager()
remote_conn.write(<command> + '\n')
remote_conn.close()
"""

import telnetlib
import time
import sys

TELNET_PORT = 23
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
remote_conn.write(password + '\n')
# Need to wait for 1 second, or output is empty; no router prompt
time.sleep(1)
output = remote_conn.read_very_eager()
print output

# Write 'show ip int brief' to router
remote_conn.write('show ip int brief' + '\n')
# Need to wait for 1 second, else output is empty
time.sleep(1)
output = remote_conn.read_very_eager()
print output

remote_conn.close()

