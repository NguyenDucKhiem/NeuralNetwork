# import numpy libraly
import numpy as np
# import matplotlib libraly
import matplotlib.pyplot as plt 
# import sys libraly
import sys

def plot(path, isShow = 0, isSave = 1, dirsave = './image.png'):
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
    
    # if save
    if isSave == 1:
        plt.savefig(dirsave, dpi=500)
    # show plot
    if isShow == 1:
        plt.show()
    
# Main
if __name__ == "__main__":
    # if No argv
    if len(sys.argv) < 2:
        # print screen no path
        print("No path!\n")
    elif len(sys.argv) == 2:
        # call plot
        plot(sys.argv[1])
    elif len(sys.argv) == 3:
        # if -s show screen and don't save image
        if sys.argv[2] == '-s':
            plot(sys.argv[1], isShow=1, isSave=0)
        # if -l don't show screen and save image
        elif sys.argv[2] == '-i':
            plot(sys.argv[1], isShow=0, isSave=1)
        # if -a show screen and save image
        elif sys.argv[2] == '-a':
            plot(sys.argv[1], isShow=1, isSave=1)
        else:
            # anything else print error
            print("error\n")
    elif len(sys.argv) == 4:
         # if -i don't show screen and save image have dir argv[2]
        if sys.argv[2] == '-i':
            plot(sys.argv[1], isShow=0, isSave=1, dirsave=sys.argv[3])
        # if -a show screen and save imagehave dir argv[2]
        elif sys.argv[2] == '-a':
            plot(sys.argv[1], isShow=1, isSave=1, dirsave=sys.argv[3])
        else:
            # anything else print error
            print("error\n")
    else:
        # anything else print error
        print('error')