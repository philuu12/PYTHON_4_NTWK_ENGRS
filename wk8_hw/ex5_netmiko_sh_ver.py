#!/usr/bin/env python

"""
5. Use Netmiko to connect to each of the devices in the database.
Execute 'show version' on each device. Calculate the amount of time required to do this.
"""

from netmiko import ConnectHandler
from datetime import datetime

from net_system.models import NetworkDevice, Credentials
import django
import ex1_link_obj_2_credentials

def main():
    django.setup()

    # Load device info and credentials into database
    ex1_link_obj_2_credentials.link_device_to_credentials()
    devices = NetworkDevice.objects.all()

    for a_device in devices:
      if a_device.device_name and a_device.credentials:
        start_time = datetime.now()
        creds = a_device.credentials
        username = creds.username
        password = creds.password
        remote_conn = ConnectHandler(device_type=a_device.device_type,
                                     ip=a_device.ip_address,
                                     username=username,
                                     password=password,       
                                     port=a_device.port,
                                     secret='')

        # Print out 'show version' output
        print
        print '#' * 80
        print ("'show version' output for device: %s" % a_device.device_name)
        print '#' * 80
        print remote_conn.send_command("show version")

        # Print out elapsed time
        print '#' * 80
        print ("Elapsed time: "  + str(datetime.now() - start_time)) 
        print '#' * 80

if __name__ == "__main__":
    main()

