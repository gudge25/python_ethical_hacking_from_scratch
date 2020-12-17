#!/usr/bin/env python2.7
import scapy.all as  scapy
from scapy.layers.l2 import arping


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]



    print("-----------------------------------------------------")
    print("|   IP\t\t\t MAC Address   |\n-----------------------------------------------------")
    #print(answered_list.summary())
    client_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc }
        client_list.append(client_dict)
        print(element[1].psrc + "\t\t" + element[1].hwsrc)
        #print(element[1].show())
    print(client_list)
# scan("192.168.100.1")
scan("192.168.100.1/24")
