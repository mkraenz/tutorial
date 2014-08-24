__author__ = 'proSingularity'

from xmlrpc.server import SimpleXMLRPCServer as server
from tut.BerechnePi_Chapter_18_3 import naehere_pi_an as pi
import sys, traceback

def add(a, b):
    return a+b
try:
    server = server(("192.168.0.108", 60000))

    server.register_function(add)
    server.register_function(pi, "pi")
    print("server started")
    server.serve_forever()
except BaseException:
    tb = sys.exc_info()
    traceback.print_tb(tb)
finally:
    server.server_close()