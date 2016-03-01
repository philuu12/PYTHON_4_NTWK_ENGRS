#!/usr/bin/env python
"""
2. Using Arista's pyeapi, create a script that allows you to add a VLAN 
(both the VLAN ID and the VLAN name).  

Your script should first check that the VLAN ID is available and only add 
the VLAN if it doesn't already exist.  Use VLAN IDs between 100 and 999.
You should be able to call the script from the command line as follows:

   python eapi_vlan.py --name blue 100     # add VLAN100, name blue

If you call the script with the --remove option, the VLAN will be removed.

   python eapi_vlan.py --remove 100          # remove VLAN100

Once again only remove the VLAN if it exists on the switch.  You will probably want
to use Python's argparse to accomplish the argument processing.

In the lab environment, if you want to directly execute your script, then you will
need to use '#!/usr/bin/env python' at the top of the script
(instead of '!#/usr/bin/python').
"""
import argparse
import pyeapi 

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", help="Name of new vlan")
parser.add_argument("-r", "--remove", help="Remove an existing vlan with specified ID number.")
parser.add_argument("vlan_id", type=int, help="Add a new vlan with specified ID number.")
args = parser.parse_args()

# Connect a Connection to Arista switch; using the switch specified in
# /home/pluu/.eapi.conf file
# cat .eapi.conf
# ----------------
# (venv)[pluu@ip-172-30-0-57 ~]$ cat .eapi.conf
# [connection:pynet-sw3]
# username: eapi
# password: ZZteslaX
# host: 50.76.53.27
# port: 8443
# transport: https
# (venv)[pluu@ip-172-30-0-57 ~]$
pynet_sw3 = pyeapi.connect_to("pynet-sw3")

#------------------------------------------------
# Adding VLAN
#------------------------------------------------
if args.name:
    vlan_name = args.name
    # See if a vlan to-be-added already exists
    try:
        pynet_sw3.enable("show vlan {vlan_id}".format(vlan_id=args.vlan_id))
    except:  
        cmds = ['vlan {vlan_id}'.format(vlan_id=args.vlan_id),
            'name {vlan_name}'.format(vlan_name=vlan_name)
           ]
        print("Creating new vlan {}...".format(args.vlan_id))
        pynet_sw3.config(cmds)
    else:
        print("VLAN {vlan_id} already exists.".format(vlan_id=args.vlan_id))
else:
    print "No vlan added."

#------------------------------------------------
# Removing VLAN
#------------------------------------------------
if args.remove:
    # See if a vlan to-be-removed exists or not 
    try:
        pynet_sw3.enable("show vlan {vlan_id}".format(vlan_id=args.vlan_id))
    except:  
        # Do not perform vlan removal if no such vlan exists (exception thrown)
        pass
    else:
        # Perform vlan removal if no exception thrown from previous block
        cmds = [ 'no vlan {vlan_id}'.format(vlan_id=args.vlan_id) ]
        print("Deleting vlan {}...".format(args.vlan_id))
        pynet_sw3.config(cmds)
else:
    print "No vlan removed."



