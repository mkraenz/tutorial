'''
Created on 20.08.2014
https://docs.python.org/3.4/library/socket.html#socket.socket.recv
@author: proSingularity
'''
import socket

def start_server():
    HOST = "localhost"
    PORT = 60000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    print("server started")
    s.listen(1)

    conn, addr = s.accept()
    print("connected by", addr)
    while True:
        data = conn.recv(1024)
        if not data: break
        conn.sendall(data)
    conn.close()