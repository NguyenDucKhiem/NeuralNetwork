import numpy as np
import csv


WeeklyInfectiousFile = '/dataset/Weekly infectious.csv'
'''

'''
def check(item):
    # print(item)
    # if item[1:-1] is 'Nan':
    #     return -1
    # elif item[1:-1] is '':
    #     return -2
    if item == '':
        return -1
    if item[0] >= '0' and item[0] <= '9':
        return int(item)
    else:
        return -3

'''
X = []
with open(WeeklyInfectiousFile, 'r') as f:
    fields = f.readline()
    lines = f.readlines()
    for line in lines:
        arr = line[:-1].split(",")
        X.append([check(item) for item in arr])
        print(X)
        break
'''


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

# X = np.loadtxt('../dataset/Weekly infectious.csv',delimiter=',', skiprows=1)