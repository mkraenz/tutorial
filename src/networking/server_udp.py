'''
Created on 20.08.2014

@author: Mirco
'''

import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    soc.bind(("", 60000))
    while True:
        (daten, address) = soc.recvfrom(1024)
        print("[%s] %s" % (address[0], daten))
finally:
    soc.close()