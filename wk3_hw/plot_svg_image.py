#!/usr/bin/env python

"""
Description of hw2 (Week 3)
--------------------------
Problem 2. Using SNMPv3 create two SVG image files.  
The first image file should graph the input and output octets on interface FA4 on pynet-rtr1
every five minutes for an hour.  Use the pygal library to create the SVG graph file.
Note, you should be doing a subtraction here (i.e. the input/output octets transmitted
during this five minute interval).  

The second SVG graph file should be the same as the first except graph the unicast packets received and transmitted.

The relevant OIDs are as follows:
('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5')
('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5')
('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5')
('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5'),
('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5')

Note, you should be able to scp (secure copy) your image file off the lab server. You can then open up the file using a browser.  For example, on MacOs I did the following (from the MacOs terminal):
scp kbyers@<hostname>:SNMP/class2/test.svg .
This copied the file from ~kbyers/SNMP/class2/test.svg to the current directory on my MAC.  

The format of the command is:
scp <remote-username>@<remote-hostname>:<remote_path>/<remote_file> .

The period at the end indicates the file should be copied to the current directory on
the local machine.

For Windows, you can use PuTTY scp
You might need to ensure that pscp.exe (putty scp) is in your Windows PATH.

Note, the example on the cornell.edu site is doing a copy of a local file to a remote server.
You would need to do the opposite i.e. copy a remote file to your local computer:

pscp <remote-username>@<remote-hostname>:<remote_path>/<remote_file> .
"""
import time
import pygal
import snmp_helper

fa4_in_octets =  []
fa4_in_packets = []
fa4_out_octets = []
fa4_out_packets = []
SLEEP_TIME = 300

# line_chart = pygal.Line()
IP = '50.76.53.27'
a_user = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'
snmp_user = (a_user, auth_key, encrypt_key)
pynet_rtr2 = (IP, 8061)

snmp_oids = (
    ('sysName', '1.3.6.1.2.1..1.5.0', None),
    ('sysUptime', '1.3.6.1.2.1.1.3.0', None),
    ('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5', None),
    ('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5', True),
    ('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5', True),
    ('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5', True),
    ('ifOutUcastPkets_fa4', '1.3.6.1.2.1.2.2.1.17.5', True),
)

# Initialize the prev_in_octets, prev_in_pkts, prev_out_octets, and prev_out_pkts
for desc, an_oid, is_count in snmp_oids:
    snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr2, snmp_user, oid=an_oid)
    output = snmp_helper.snmp_extract(snmp_data)
    print "Initial values for Previous time-stamps: %s %s" % (desc, output)

    if desc == "ifInOctets_fa4":
        prev_in_octets = int(output)
    elif desc == "ifInUcastPkts_fa4":
        prev_in_pkts = int(output)
    elif desc == "ifOutOctets_fa4":
        prev_out_octets = int(output)
    elif desc == "ifOutUcastPkets_fa4":
        prev_out_pkts = int(output)

# Sampling input/output data (in octets/packets) every 5 minutes for 1 hour
for i in xrange(12):
    # Sleep for some regular interval before sampling data again
    print "Sleep {} seconds before sampling data again".format(SLEEP_TIME)
    time.sleep(SLEEP_TIME)

    for desc, an_oid, is_count in snmp_oids:
        snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr2, snmp_user, oid=an_oid)
        output = snmp_helper.snmp_extract(snmp_data)
        print "%s %s" % (desc, output)

        if desc == "ifInOctets_fa4":
            cur_in_octets = output
            num_in_octets = cur_in_octets - prev_in_octets
            prev_in_octets = cur_in_octets
            fa4_in_octets.append(num_in_octets)
        elif desc == "ifInUcastPkts_fa4":
            cur_in_pkts = output
            num_in_pkts = cur_in_pkts - prev_in_pkts
            prev_in_pkts = cur_in_pkts
            fa4_in_packets.append(num_in_pkts)
        elif desc == "ifOutOctets_fa4":
            cur_out_octets = output
            num_out_octets = cur_out_octets - prev_out_octets
            prev_out_octets = cur_out_octets
            fa4_out_octets.append(num_out_octets)
        elif desc == "ifOutUcastPkets_fa4":
            cur_out_pkts = output
            num_out_pkts = cur_out_pkts - prev_out_pkts
            prev_out_pkts = cur_out_pkts
            fa4_out_packets.append(num_out_pkts)

    print "======================"

#----------------------------------
# Graph packet line
pkts_line_chart = pygal.Line()
pkts_line_chart.title = 'Input and Output Packets'
pkts_line_chart.x_labels = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60']
pkts_line_chart.add('InPackets', fa4_in_packets)
pkts_line_chart.add('OutPackets', fa4_out_packets)
pkts_line_chart.render_to_file('packet_image_chart.svg')

#----------------------------------
# Graph octet (byte) line
octet_line_chart = pygal.Line()

octet_line_chart.title = 'Input and Output Bytes'
octet_line_chart.x_labels = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60']
octet_line_chart.add('InBytes', fa4_in_octets)
octet_line_chart.add('OutBytes', fa4_out_octets)
octet_line_chart.render_to_file('octet_image_chart.svg')


