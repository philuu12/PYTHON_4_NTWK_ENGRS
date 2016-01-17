#!/usr/bin/env python
from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco.txt")
crypto_map = cisco_cfg.find_objects(r"^crypto map")

print "--- WEEK 1: HW 8 ---"
""" Input for hw 6i:
The script should find all of the crypto map entries in the file
(lines that begin with 'crypto map CRYPTO') and for each crypto map entry, 
print out its children.
----------
crypto map CRYPTO 10 ipsec-isakmp 
 set peer 1.1.1.1
 set transform-set AES-SHA 
 set pfs group5
 match address VPN-TEST1
crypto map CRYPTO 20 ipsec-isakmp 
 set peer 2.2.2.1
 set transform-set AES-SHA 
 set pfs group2
 match address VPN-TEST2
crypto map CRYPTO 30 ipsec-isakmp 
 set peer 3.3.3.1
 set transform-set AES-SHA 
 set pfs group2
 match address VPN-TEST3
crypto map CRYPTO 40 ipsec-isakmp 
 set peer 4.4.4.1
 set transform-set AES-SHA 
 set pfs group5
 match address VPN-TEST4
crypto map CRYPTO 50 ipsec-isakmp 
 set peer 5.5.5.1
 set transform-set 3DES-SHA 
 set pfs group5
 match address VPN-TEST5
"""

for cm in crypto_map:
    # print out crypto map entry
    print cm.text 
    for child in cm.children:
        # print out content (children) of each crypto map entry
        print child.text

print "\n\n--- WEEK 1: HW 9 ---"
""" Input for hw 9:
Find all of the crypto map entries that are using "pfs group2"
crypto map CRYPTO 20 ipsec-isakmp 
 set peer 2.2.2.1
 set transform-set AES-SHA 
 set pfs group2
 match address VPN-TEST2
crypto map CRYPTO 30 ipsec-isakmp 
 set peer 3.3.3.1
 set transform-set AES-SHA 
 set pfs group2
 match address VPN-TEST3
"""
pfs_group2 = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map", childspec=r"pfs group2")

for i in pfs_group2:
    # print out pfs group2 entry
    print i.text
    for child in i.children:
        # print out children content of each 'pfs group2' entry
        print child.text

print "\n\n--- WEEK 1: HW 10 ---"
""" Input for hw 10:
Using ciscoconfparse find the crypto maps that are not using AES
(based-on the transform set name).
Print these entries and their corresponding transform set name
------
crypto map CRYPTO 50 ipsec-isakmp 
 set peer 5.5.5.1
 set transform-set 3DES-SHA 
 set pfs group5
 match address VPN-TEST5
"""
non_aes_sha = cisco_cfg.find_objects_wo_child(parentspec=r"crypto map", childspec=r"AES-SHA")

for each_crypto_entry in non_aes_sha:
    # Print out each crypto map entry
    print each_crypto_entry.text
    # Print out child content of each crypto map entry
    for i in each_crypto_entry.all_children: 
        print i.text



