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

def telnet_connect(ip_addr):
    try:
        remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    except socket.timeout:
        sys.exit("Connection timed-out")
    return remote_conn

def login(remote_conn, username, password):
    # Input username
    remote_conn.read_until("sername", TELNET_TIMEOUT)
    remote_conn.write(username + '\n')

    # Input password
    remote_conn.read_until("ssword:", TELNET_TIMEOUT)
    remote_conn.write(password + '\n')

def send_command(remote_conn, cmd):
    cmd = cmd.rstrip() + '\n'
    remote_conn.write(cmd)
    time.sleep(1)
    return remote_conn.read_very_eager()

def main():
    remote_conn = telnet_connect(ip_addr)
    login(remote_conn, username, password)
    output = send_command(remote_conn, "show ip int brief")
    print "Output of 'show ip int brief':", output
    remote_conn.close()
    
if __name__ == "__main__":
    main()



