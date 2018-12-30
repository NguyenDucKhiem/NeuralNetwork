# import numpy libraly
import numpy as np
# import matplotlib libraly
import matplotlib.pyplot as plt 
# import sys libraly
import sys

def plot(path):
    '''
    read data result after train and plot them\n
    path: path file result.csv 
    '''
    # print screen path plot
    print("plot with {}\n".format(path))
    # read data
    data = np.loadtxt(path, delimiter=',', skiprows=1)
    # X: week 
    X = (data[:,0:1] - 2010) * 53 + data[:,1:2]
    # patient data
    patient = data[:,4:5]
    # result data after training
    result = data[:,5:6]
    # plot patient data
    plt.plot(X, patient)
    # plot result data
    plt.plot(X, result)
    # X label
    plt.xlabel('week')
    # Y label
    plt.ylabel('number patient')
    # suptitle plot
    plt.suptitle('Patient and result affter trainng')
    # show plot
    plt.show()

# Main
if __name__ == "__main__":
    # if No argv
    if len(sys.argv) < 2:
        # print screen no path
        print("No path!\n")
    else:
        # foreach path
        for i in range(1, len(sys.argv)):
            # call plot
            plot(sys.argv[i])