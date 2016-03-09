#!/usr/bin/env python

"""
7. Repeat exercise #6 except use processes. 
"""

from netmiko import ConnectHandler
from datetime import datetime

from net_system.models import NetworkDevice, Credentials
import django

from multiprocessing import Process, current_process, Queue
import time

import ex1_link_obj_2_credentials

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
    start_time = datetime.now()

    # Load device info and credentials into database
    ex1_link_obj_2_credentials.link_device_to_credentials()
    devices = NetworkDevice.objects.all()

    procs = []
    for a_device in devices:
        print a_device, a_device.credentials

    for a_device in devices:
        my_proc = Process(target=show_version, args=(a_device,))
        my_proc.start()
        procs.append(my_proc)

    # Make sure all child processes finish running and return before proceeding
    for a_proc in procs:
        a_proc.join()     # Wait for a process to complete

    print "\nElapsed time: " + str(datetime.now() - start_time)

if __name__ == "__main__":
    main()

