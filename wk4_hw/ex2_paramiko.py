#!/usr/bin/env python
"""
Assignment 2:
Use Paramiko to change the 'logging buffered <size>' configuration on pynet-rtr2. This will require that you enter into configuration mode.
"""

import time
import paramiko
from getpass import getpass

#------------ Begin setup -----------------
ip_addr = '50.76.53.27'
username = 'pyclass'
# password = getpass()
password = '88newclass'
port = 8022

# Create SSH client object
remote_conn_pre = paramiko.SSHClient()

# Instruct Paramiko how to handle host-key
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Load the host-keys from system file .ssh/known_hosts
remote_conn_pre.load_system_host_keys()

# Create SSH connection to router
remote_conn_pre.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)

# Make Cisco devices not to close the SSH session when Paramiko closes SSH channel
remote_conn = remote_conn_pre.invoke_shell()
#------------ End setup -----------------


#------------ Begin configuring -----------------
# Turn off paging
remote_conn.send("terminal length 0\n")

# Send command down the SSH channel
remote_conn.send("configure terminal\n")
remote_conn.send("logging buffered 25000\n")

# show running-config
remote_conn.send("exit\n")
remote_conn.send("show running-config\n")

# Sleep for 1 second for the data to show up
time.sleep(1)

# Set the number of bytes to be received back and read data back
outp = remote_conn.recv(60000)

# Display output of command 'show runn'
print outp

# Restore the original setting
outp = remote_conn.send("logging buffered 20000\n")

#------------ End configuring -----------------


