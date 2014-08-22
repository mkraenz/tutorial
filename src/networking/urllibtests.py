'''
Created on 21.08.2014

@author: Mirco
'''

import urllib.request
f = urllib.request.urlopen("https://www.google.de")
data = open("google.de.html", "w")
for row in f:
    data.write(row.decode())