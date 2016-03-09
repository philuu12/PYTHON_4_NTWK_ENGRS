#!/usr/bin/env python

"""
1. Initialize your Django database. Add the seven NetworkDevice objects and
two Credentials objects into your database.  After this initialization,
you should be able to do the following (from the ~/DJANGOX/djproject directory):

$ python manage.py shell

>>> from net_system.models import NetworkDevice, Credentials
>>> net_devices = NetworkDevice.objects.all()
>>> net_devices
[<NetworkDevice: pynet-rtr1>, <NetworkDevice: pynet-sw1>, <NetworkDevice: pynet-sw2>,
<NetworkDevice: pynet-sw3>, <NetworkDevice: pynet-sw4>, <NetworkDevice: juniper-srx>,
<NetworkDevice: pynet-rtr2>]

>>> creds = Credentials.objects.all()
>>> creds
[<Credentials: pyclass>, <Credentials: admin1>]
"""

from net_system.models import NetworkDevice, Credentials

def link_device_to_credentials():
    devices = NetworkDevice.objects.all()
    creds = Credentials.objects.all()

    # Cisco credentials
    std_creds = creds[0]

    # Arista credentials
    arista_creds = creds[1]
    
    for a_device in devices:
        if 'pynet-sw' in a_device.device_name:
            a_device.credentials = arista_creds
        else:
            a_device.credentials = std_creds

        # Save device credentials in the database
        a_device.save()

    for a_device in devices:
        print a_device, a_device.credentials

def main():
    link_device_to_credentials()

if __name__ == "__main__":
    main()

