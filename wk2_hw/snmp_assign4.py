#!/usr/bin/env python

from snmp_helper import snmp_get_oid, snmp_extract

# Beginning of setup
COMMUNITY_STRING = 'galileo'
RT1_SNMP_PORT = 7961
RT2_SNMP_PORT = 8061
IP = '50.76.53.27'

pynet_router1 = (IP, COMMUNITY_STRING, RT1_SNMP_PORT)
pynet_router2 = (IP, COMMUNITY_STRING, RT2_SNMP_PORT)

OID_sysName = "1.3.6.1.2.1.1.5.0"
OID_sysDescr = "1.3.6.1.2.1.1.1.0"
# End of setup

snmp_sysName = snmp_get_oid(pynet_router1, oid=OID_sysName)
snmp_sysDescr = snmp_get_oid(pynet_router1, oid=OID_sysDescr)

sysName = snmp_extract(snmp_sysName)
sysDescr = snmp_extract(snmp_sysDescr)

print "Router 1: %s\nSystem name: %s\nSystem Description: %s" % \
    (pynet_router1, sysName, sysDescr)

print "\n========================"
snmp_sysName = snmp_get_oid(pynet_router2, oid=OID_sysName)
snmp_sysDescr = snmp_get_oid(pynet_router2, oid=OID_sysDescr)

sysName = snmp_extract(snmp_sysName)
sysDescr = snmp_extract(snmp_sysDescr)

print "Router 2: %s\nSystem name: %s\nSystem Description: %s" % \
    (pynet_router2, sysName, sysDescr)

