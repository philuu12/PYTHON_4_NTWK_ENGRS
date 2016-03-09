#!/usr/bin/env python

"""
6. Use threads and Netmiko to execute 'show version' on each device in the
database. Calculate the amount of time required to do this. What is
the difference in time between executing 'show version' sequentially versus
using threads?
"""

from netmiko import ConnectHandler
from datetime import datetime

from net_system.models import NetworkDevice, Credentials
import ex1_link_obj_2_credentials
import django
import threading
import time

def show_version(a_device):
    creds = a_device.credentials
    remote_conn = ConnectHandler(device_type=a_device.device_type,
                                 ip=a_device.ip_address,
                                 username=creds.username,
                                 password=creds.password,
                                 port=a_device.port,
                                 secret='')

    print
    print '#' * 80
    print remote_conn.send_command("show version")
    print '#' * 80

def main():
    django.setup()

    # Load device info and credentials into database
    ex1_link_obj_2_credentials.link_device_to_credentials()
    devices = NetworkDevice.objects.all()

    start_time = datetime.now()
    print "Print out device info: "
    for a_device in devices:
        print a_device, a_device.credentials

    for a_device in devices:
        my_thread = threading.Thread(target=show_version, args=(a_device,))
        my_thread.start()

    main_thread = threading.currentThread()
    for a_thread in threading.enumerate():
        if a_thread != main_thread:
            print a_thread
            a_thread.join()     # Wait for a thread to complete

    print "\nElapsed time: " + str(datetime.now() - start_time)

if __name__ == "__main__":
    main()

