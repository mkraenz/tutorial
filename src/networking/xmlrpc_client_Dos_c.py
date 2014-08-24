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


    def __init__(self, params=None):
        threading.Thread.__init__(self, params)
        
        
    def run(self):
        proxy = prox("http://198.168.0.108:60000")
        proxy.add(1,2)
    
