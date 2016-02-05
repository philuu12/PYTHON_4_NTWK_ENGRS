#!/usr/bin/env python

import pygal
fa4_in_octets =   [5269, 5011, 6705, 5987, 5011, 5071, 6451, 5011, 5011, 6181, 5281, 5011]
fa4_out_octets = [5725, 5783, 7670, 6783, 5398, 5783, 9219, 3402, 5783, 6953, 5668, 5783]

fa4_in_packets =   [24, 21, 40, 32, 21, 21, 49, 9, 21, 34, 24, 21]
fa4_out_packets = [24, 21, 40, 32, 21, 21, 49, 9, 21, 34, 24, 21]

line_chart = pygal.Line()

line_chart.title = 'Input/Output Packets and Bytes'
line_chart.x_labels = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60']
line_chart.add('InPackets', fa4_in_packets)
line_chart.add('OutPackets', fa4_out_packets)
line_chart.add('InBytes', fa4_in_octets)
line_chart.add('OutBytes', fa4_out_octets)

line_chart.render_to_file('test.svg')


