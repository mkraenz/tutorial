__author__ = 'proSingularity'

from xmlrpc.client import ServerProxy as prox
import random

proxy = prox("http://192.168.0.108:60000")
print("rpc client started.")
res = proxy.add(1,2)
print("result =", res)

print(proxy.pi(10000))