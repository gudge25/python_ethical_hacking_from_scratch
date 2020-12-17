#!/usr/bin/env python2.7
import scapy.all as  scapy
from scapy.layers.l2 import arping


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    arp_request.show()
    # arp_request.pdst=ip
    # arping(ip)
    # print(arp_request.summary())
    # scapy.ls(scapy.ARP())
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # scapy.ls(scapy.Ether())
    broadcast.show()
    arp_request_broadcast = broadcast / arp_request
    # print(arp_request_broadcast.summary())
    arp_request_broadcast.show()


# scan("192.168.100.1")
scan("192.168.100.1/24")
