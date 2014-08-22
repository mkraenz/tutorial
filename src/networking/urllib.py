'''
Created on 21.08.2014

@author: Mirco
'''

import urllib

w = urllib.request.urlopen("http://google.com")
p = w.read()
print(p)