'''
Created on 20.08.2014

@author: Mirco
'''
import socket

addr = ip,port = "192.168.0.120", 60000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(addr)

try:
    while True:
        message = input("Message: ").encode(encoding='utf_8', errors='strict')
        s.send(message)
        answer = s.recv(1024)
        print("[%s] %s" % (ip,answer))
finally:
    s.close()