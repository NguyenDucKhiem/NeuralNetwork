import numpy as np
import csv


WeeklyInfectiousFile = 'dataset/Weekly infectious.csv'
'''

'''
def check(item):
    if item == '':
        return -1
    if item[0] >= '0' and item[0] <= '9':
        return int(item)
    else:
        return -3



IndexInput = 1
IndexOutput = 40
# import pandas

X = [[],[]]
Y = []
# Doc file row 2 va 41
with open(WeeklyInfectiousFile, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        X = np.append(X, [[check(row[IndexInput])],[1]], axis=1)
        Y = np.append(Y, [check(row[IndexOutput])], axis=0)

print(X)
