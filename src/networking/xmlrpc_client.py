__author__ = 'proSingularity'

from xmlrpc.client import ServerProxy as prox
import random

proxy = prox("http://localhost:60000")
print("rpc client started.")
res = proxy.add(1,2)
print("result =", res)

print(proxy.pi(100000000))