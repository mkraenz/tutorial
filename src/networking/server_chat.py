'''
Created on 20.08.2014

@author: proSingularity
'''

import socket, _thread


def receive(comm, addr):
    while True:
        data = comm.recv(1024)

        print("[%s] %s" % (addr[0], data.decode()))


def send(comm):
    while True:
        message = input("message: ").encode()
        comm.send(message)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 60000))
s.listen(1)
try:
    while True:
        comm, addr = s.accept()
        _thread.start_new_thread(receive, (comm, addr))
        _thread.start_new_thread(send, (comm,))

finally:
    s.close()