#!/usr/bin/env python
'''
Write a script using a telnet_device class that connects to the lab pynet-rtr1, logins, and executes the
'show ip int brief' command.
'''

import pysnmp
from snmp_helper import snmp_get_oid, snmp_extract
from pysnmp.entity.rfc3413.oneliner import cmdgen


def snmpwalkgen(ipaddr,commst,oid,port=161):
    cmdGen = cmdgen.CommandGenerator()
    errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.nextCmd(cmdgen.CommunityData(commst),cmdgen.UdpTransportTarget((ipaddr,port)),oid,lookupNames=True, lookupValues=True)
    walk_results=[]
    if errorIndication:
        print(errorIndication)
    else:
        if errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),errorIndex and varBindTable[-1][int(errorIndex)-1] or '?'))
        else:
            for varBindTableRow in varBindTable:
                for name, val in varBindTableRow:
                    walk_results.append([name.prettyPrint(), val.prettyPrint()])
#                    print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
    return walk_results


class SnmpDevice(object):
    def __init__(self,ipaddr,commst,port=161):
        self.ipaddr=ipaddr
        self.commst=commst
        self.port=port
        self.device=(ipaddr,commst,port)
    def snmpget(self,oid):
        return snmp_extract(snmp_get_oid(self.device,oid))
    def snmpwalk(self,oid):
        return snmpwalkgen(self.ipaddr,self.commst,oid,self.port)
    def get_sysname(self,force=False):
        if force or not hasattr(self,'sysname'):
            self.sysname=self.snmpget('1.3.6.1.2.1.1.5.0')
        return self.sysname
    def get_sysdesc(self,force=False):
        if force or not hasattr(self,'sysdesc'):
            self.sysdesc=self.snmpget('1.3.6.1.2.1.1.1.0')
        return self.sysdesc
    def get_sysoid(self,force=False):
        if force or not hasattr(self,'sysoid'):
            self.sysoid=self.snmpget('1.3.6.1.2.1.1.2.0')
        return self.sysoid
    def walk_iftable(self,force=False):
        if force or not hasattr(self,'iftable'):
            self.iftable=self.snmpwalk('1.3.6.1.2.1.2.2')
        return self.iftable

def main():
    community_string='galileo'
    ipaddr='50.76.53.27'
    iftable_oid='1.3.6.1.2.1.2.2'
    rtr1=SnmpDevice(ipaddr,community_string,7961)
    rtr2=SnmpDevice(ipaddr,community_string,8061)
    print '\n\n',rtr1.get_sysname(),'\n', rtr1.get_sysdesc()
    print '\n\n',rtr2.get_sysname(), '\n',rtr2.get_sysdesc()
    print '\n\n',rtr1.snmpwalk(iftable_oid),'\n'
    print '\n\n',rtr2.walk_iftable(),'\n'

if __name__=="__main__":
    main()


