#!/usr/bin/env python
"""
Assignment 3:
Use Pexpect to retrieve the output of 'show ip int brief' from pynet-rtr2.
"""
import pexpect
import re
from getpass import getpass

def main():
    ip_addr ='50.76.53.27'
    username = 'pyclass'
    port = 8022
    password = getpass()        # password: 88newclass

    # Spawn a child process
    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))

    # Set time out (in seconds)
    ssh_conn.timeout = 5 

    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)

    ssh_conn.expect('#')

    ssh_conn.sendline("show ip int brief")
    ssh_conn.expect("#")

    # Print out texts before last expect command ('#')
    print ssh_conn.before

if __name__ == "__main__":
    main()

