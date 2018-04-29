#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
from functools import reduce
import struct

# 取IP为76.16.17.81~76.16.17.84之外的所有IP
def ip2num(addr):
    # parse the address string into integer quads
    # quads = map(ord, socket.inet_aton(addr))
    quads = map(lambda x: ord(chr(x)), socket.inet_aton(addr))
    # spread the quads out
    return reduce(lambda x,y: x * 0x100 + y, quads)

def num2ip(num):
    return "%d.%d.%d.%d" % (num/0x1000000, num%0x1000000/0x10000, num%0x10000/0x100, num%0x100)

#num2ip(ip2num("76.16.17.81"))

upper_bound = ip2num("76.16.17.84")
lower_bound = ip2num("76.16.17.81")

for i in range(ip2num("255.255.255.255")):
    if i > upper_bound or i < lower_bound:
        print(num2ip(i))
