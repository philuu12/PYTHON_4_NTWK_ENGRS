#!/usr/bin/env python
"""
3. Create two new test NetworkDevices in the database. Use both direct 
object creation and the .get_or_create() method to create the devices.
"""

from net_system.models import NetworkDevice
import django

def main():
    django.setup()

    brocade_rtr1 = NetworkDevice(
        device_name='Brocade-rtr1',
        device_type='fc_san',
        ip_address='50.76.53.28',
        port=8022,
    )

    hp_sw1 = NetworkDevice(
        device_name='HP-sw1',
        device_type='stratus',
        ip_address='50.76.53.29',
        port=8022,
    )

    # Save new device information in database
    brocade_rtr1.save()
    hp_sw1.save()

    # Print out devices just added
    for a_dev in (brocade_rtr1, hp_sw1):
        print a_dev

    print "Display devices in the database"
    devices = NetworkDevice.objects.all()
    for a_device in devices:
        print a_device.device_name

if __name__ == "__main__":
    main()

