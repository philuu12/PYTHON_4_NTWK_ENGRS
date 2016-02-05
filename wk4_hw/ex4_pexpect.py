#!/usr/bin/env python
"""
Assignment 4:
Use Pexpect to change the logging buffer size (logging buffered <size>) on pynet-rtr2. Verify this change by examining the output of 'show run'.
"""
import pexpect
import re
from getpass import getpass

def main():
    ip_addr = '50.76.53.27'
    username = 'pyclass'
    port = 8022
    password = getpass()

    # Spawn a child process
    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))

    # Set time out
    ssh_conn.timeout = 3
    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)

    ssh_conn.expect("#")
    
    # Set logging buffered to 25000
    ssh_conn.sendline("configure terminal")
    ssh_conn.sendline("logging buffered 25000")

    # Search for pattern "logging buffered 25000" in 'show runn' output
    pattern = re.compile(r'logging buffered 25000', re.MULTILINE)
    ssh_conn.sendline("show running-config")
    ssh_conn.expect(pattern)

    print "The found matching pattern is:"
    print ssh_conn.after

    # Restoring the setting back to 20000
    ssh_conn.sendline("configure terminal")
    ssh_conn.sendline("logging buffered 20000")

if __name__ == "__main__":
    main()

    
