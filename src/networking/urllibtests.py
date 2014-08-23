'''
Created on 21.08.2014

@author: Mirco
'''

import urllib.request

f = urllib.request.urlopen(
    "file:///C:/Users/Mirco/Desktop/galileocomputing_python/python_kapitel_20_002.htm#mjdb126d022da9199ad232014227ef993f")
data = open("networkingchapter.htm", "w")
for row in f:
    data.write(row.decode("utf8", "ignore"))