'''
Created on 19.08.2014

@author: proSingularity
'''

import csv

writer = csv.writer(open("E:/Python Workspace/LUDecomposition/Tests/matr.csv", "w", newline=''))
"""
data = [1,3]
writer.writerow(data)
"""
writer.writerow(["marke", "modell", "leistung_in_ps"])