#!/usr/bin/env python

"""
Assignment 1:
Use Paramiko to retrieve the entire 'show version' output from pynet-rtr2
"""
import paramiko
import time
from getpass import getpass

ip_addr = '50.76.53.27'
username = 'pyclass'
password = getpass()
port = 8022                     # Router pynet-rtr2 port

# Create an SSH client object
remote_conn_pre=paramiko.SSHClient()

# Tell paramiko to accept any host-key (might be security concern?)
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.load_system_host_keys()

# Create an SSH connection to device
remote_conn_pre.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)

remote_conn = remote_conn_pre.invoke_shell()

#----------------------------------------------------------------
# Read entire 'show version' output back from pynet-rtr2 router
#----------------------------------------------------------------

# 0. Turn off paging
outp = remote_conn.send("terminal length 0\n")
# 1. Send the command down the channel
remote_conn.send("show version\n")
time.sleep(2)
# 2. Read back from ssh channel
outp  = remote_conn.recv(5000)      # Read back 5000 bytes
# 3. Print out the result
print outp


