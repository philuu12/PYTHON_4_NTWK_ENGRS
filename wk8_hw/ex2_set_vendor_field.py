#!/usr/bin/env python
"""
2. Set the vendor field of each NetworkDevice to the appropriate vendor.
Save this field to the database.
"""

from net_system.models import NetworkDevice, Credentials


def main():
    devices = NetworkDevice.objects.all()
    creds = Credentials.objects.all()

    # Cisco credentials
    std_creds = creds[0]

    # Arista credentials
    arista_creds = creds[1]
    
    for a_device in devices:
        if 'pynet-sw' in a_device.device_name:
            a_device.vendor = 'Arista'
        elif 'pynet-rtr' in a_device.device_name:
            a_device.vendor = 'Cisco' 
        else:
            a_device.vendor = 'Juniper'

        # Save device info in the database
        a_device.save()

    for a_device in devices:
        print a_device, a_device.vendor

if __name__ == "__main__":
    main()

