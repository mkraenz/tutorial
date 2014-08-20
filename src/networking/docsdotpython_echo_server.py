'''
Created on 20.08.2014
https://docs.python.org/3.4/library/socket.html#socket.socket.recv
@author: Mirco
'''
import socket

HOST = "localhost"
PORT = 60000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print("connected by", addr)
while True:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)
conn.close()