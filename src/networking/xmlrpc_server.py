__author__ = 'proSingularity'

from xmlrpc.server import SimpleXMLRPCServer as server
from src.tut.BerechnePi_Chapter_18_3 import naehere_pi_an as pi
def add(a, b):
    return a+b
try:
    server = server(("", 60000))

    server.register_function(add)
    server.register_function(pi, "pi")
    print("server started")
    server.serve_forever()
finally:
    server.server_close()