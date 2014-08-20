'''
Created on 20.08.2014
https://docs.python.org/3.4/library/socket.html#socket.socket.recv
@author: Mirco
'''
import socket

HOST = "localhost"
PORT = 60000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((HOST, PORT))
    s.sendall(b"Hi There")
    data = s.recv(1024)
    print("received:". repr(data))
finally:
    s.close()