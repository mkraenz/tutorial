'''
Created on 20.08.2014

@author: proSingularity
'''

import socket

ip = "localhost"
soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    while True:
        message = input("Enter new message: ")
        if (message == "exit"):
            break
        soc.sendto(message.encode(encoding='utf_8', errors='strict'),
                   (ip, 60000))
finally:
    soc.close()