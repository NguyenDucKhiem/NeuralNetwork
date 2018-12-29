# import numpy libraly
import numpy as np
# import csv libraly
import csv

# path file and number row read patient file
WeeklyInfectiousFile = ['dataset/Weekly infectious.csv', 0, 1, 40]
# path file and number row read psi file
PSIFile = ['dataset/psi.csv', 0, 1, 2, 4, 5, 6, 7]
# path file and number row read rain file
RainFile = ['dataset/rainfall-monthly-number-of-rain-days.csv', 0, 1, 2]



def check(item):
    '''
    function check item\n
    if item is empty => return -1\n
    if item[0] is number => return number of item\n
    anything else return -2
    '''
    # if none return error -1
    if item == '':
        return -1
    # if item is number, return number
    if item[0] >= '0' and item[0] <= '9':
        return int(item)
    # anything else return error -2
    else:
        return -2

def Read(readFile):
    '''
    function read file according to the column number\n
    readFile: array, first element is path file, continue is number row read\n
    return matrix in readFile
    '''
    # init matrix answer
    ret =[]
    # open file
    with open(readFile[0], 'r') as csvfile:
        # read file
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            # if exists row[i] < 0 flag = 1 else flag = 0
            flag = 0
            # init input
            matrix = []
            # foreach matrix data
            for i in readFile[1:]:
                # check and return item
                value = check(row[i])
                # if value < 0 break and don't append ret
                if value > 0:
                    # append value into matrix
                    matrix.append(value)
                else:
                    # flag unknown data
                    flag = 1
                    break

            # append ret if known data
            if not flag:
                # append result
                ret.append(matrix)
        # transpose result
        ret = np.transpose(ret)
    # return result
    return ret