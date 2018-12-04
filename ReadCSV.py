import numpy as np
import csv
# import pandas
# file dataset
WeeklyInfectiousFile = ['dataset/Weekly infectious.csv', 0, 1, 40]
PSIFile = ['dataset\psi.csv', 0, 1, 2, 4, 5, 6, 7] # index 3 how to convert 4p.m to int??
RainFile = ['dataset\rainfall-monthly-number-of-rain-days.csv', 0, 1, 2]
Weather = ['dataset\weather.csv']   


# function check item
# if item is empty => return -1
# if item[0] is number => return number of item
# anything else return -2
def check(item):
    if item == '':
        return -1
    if item[0] >= '0' and item[0] <= '9':
        return int(item)
    else:
        return -2
# end function check(item)

# function Read
# reaturn matrix in readFile
def Read(readFile):
    # matrix answer
    ret = []
    with open(readFile[0], 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            # if exists row[i] < 0 flag = 1 else flag = 0
            flag = 0
            # init matrix
            matrix = []
            for i in readFile[1:]:
                value = check(row[i])
                # if value < 0 break and don't append ret
                if value > 0:
                    matrix.append(value)
                else:
                    flag = 1
                    break

            # append ret
            if not flag:
                ret.append(matrix)
    # transpose matrix
    ret = np.transpose(ret)
    return ret

# Check class
# R = ReadCSV()
# X = R.Read(WeeklyInfectiousFile)

# print(X)