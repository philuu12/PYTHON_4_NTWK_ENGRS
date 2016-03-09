#!/usr/bin/env python

"""
4. Remove the two objects created in the previous exercise from the database.
"""

from net_system.models import NetworkDevice
import django

def main():
    django.setup()
    """
    # Add 2 new devices: Brocade and HP to database
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
    """
    devices = NetworkDevice.objects.all()

    print
    print '#' * 80
    print "Display devices prior to Deletion"
    print '#' * 80
    for a_device in devices:
        print a_device.device_name

    print 
    print '#' * 80
    print "Deleting Brocade and HP network devices"
    print '#' * 80
    for a_device in devices:
        if  'HP-sw' in a_device.device_name or \
            'Brocade-rtr' in a_device.device_name:
            print("Delete device: ", a_device.device_name)
            a_device.delete()

    print
    print '#' * 80
    print "Display devices post Deletion"
    print '#' * 80
    for a_device in devices:
        if a_device.device_name:
            print a_device.device_name

if __name__ == "__main__":
    main()

