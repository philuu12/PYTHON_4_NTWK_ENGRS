#!/usr/bin/env python

"""
8. Optional bonus question -- use a queue to get the output data back from
the child processes in question #7. Print this output data to the screen
in the main process.
"""

from netmiko import ConnectHandler
from datetime import datetime

from net_system.models import NetworkDevice, Credentials
import django

from multiprocessing import Process, current_process, Queue
import time

import ex1_link_obj_2_credentials

def show_version_queue(a_device, q):
    #creds = a_device.credentials
    output_dict = {}
    remote_conn = ConnectHandler(device_type=a_device.device_type,
                                 ip=a_device.ip_address,
                                 username=a_device.credentials.username,
                                 password=a_device.credentials.password,
                                 port=a_device.port,
                                 secret='')

    # print '#' * 80
    output = ('#' * 80) + "\n"
    # print remote_conn.send_command("show version")
    output += remote_conn.send_command("show version") + "\n" 
    # print '#' * 80
    output += ('#' * 80) + "\n"

    output_dict[a_device.device_name] = output
    q.put(output_dict)                  # Add to the queue

def main():
    django.setup()
    start_time = datetime.now()
    q = Queue(maxsize=20)

    # Load device info and credentials into database
    ex1_link_obj_2_credentials.link_device_to_credentials()
    devices = NetworkDevice.objects.all()

    procs = []
    for a_device in devices:
        print a_device, a_device.credentials

    for a_device in devices:
        my_proc = Process(target=show_version_queue, args=(a_device, q))
        my_proc.start()
        procs.append(my_proc)

    # Make sure all child processes finish running and return before proceeding
    for a_proc in procs:
        a_proc.join()     # Wait for a process to complete

    while not q.empty():
        my_dict = q.get()
        for k,v in my_dict.iteritems():
            print k
            print v

    print "\nElapsed time: " + str(datetime.now() - start_time)

if __name__ == "__main__":
    main()

