'''
Created on 20.08.2014

@author: Mirco
'''

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("getfqdn", socket.getfqdn())
print("gethostname", socket.gethostname())
print("gethostbyname:", socket.gethostbyname("www.google.de"))
print("gethostbyname:", socket.gethostbyname("www.google.com"))
