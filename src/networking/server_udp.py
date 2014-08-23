'''
Created on 20.08.2014

@author: proSingularity
'''

import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    soc.bind(("192.168.0.120", 60000))
    while True:
        (daten, address) = soc.recvfrom(1024)
        print("[%s] %s" % (address[0], daten))
        soc.sendto(b"thanks", ("192.168.0.100", 60000))
finally:
    soc.close()