#!/usr/bin/env python2.7

from scapy.layers.l2 import arping


def scan(ip):
    arping(ip)


#scan("192.168.100.1")
scan("192.168.100.1/24")
