'''
Created on 20.08.2014

@author: Mirco
'''

import socket, _thread

addr = ip,port = "192.168.0.120", 60000

def receive(comm, addr):
    while True:
        data = comm.recv(1024)
        
        print("[%s]: %s" % addr[0], data.decode())
        
def send(comm):
    while True:
        message = input("message: ")
        comm.send(message.encode())
    


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(addr)

try:
    _thread.start_new_thread(receive, (s, addr))
    _thread.start_new_thread(send, (s,))
    while True:
        pass
finally:
    s.close()