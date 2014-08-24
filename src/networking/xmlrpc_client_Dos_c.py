'''
Created on 24.08.2014

@author: proSingularity
'''
from xmlrpc.client import ServerProxy as prox
import threading

class Dos(threading.Thread):
    '''
    classdocs
    '''


    def __init__(self, params):
        threading.Thread.__init__(self)
        
        
    def run(self):
        proxy = prox("198.168.0.100:60000")
        proxy.add(1,2)
    
