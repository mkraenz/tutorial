'''
Created on 20.08.2014

@author: Mirco
'''

import socket

ip = "localhost"
message = b"ich bin ein packet vom client"
soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    soc.sendto(message, (ip, 60000))
finally:
    soc.close()