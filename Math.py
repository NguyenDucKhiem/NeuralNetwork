import math
import numpy as np

def ReLU(x):
    '''
    function ReLU
    
    Arguments:
    x -- real

    Return:
    value of function ReLU with x
    '''
    return np.maximum(x, 0)

def DerivativeReLU(x):
    '''
    function derivative ReLU
    
    Arguments:
    x -- real

    Return:
    value of function derivative ReLU with x
    '''
    return np.greater(x, 0).astype(int)

def basic_sigmoid(x):
    """
    Compute sigmoid of x.

    Arguments:
    x -- A scalar or numpy array of any size

    Return:
    s -- sigmoid(x)
    """

    ### START CODE HERE ### (≈ 1 line of code)
    s = 1./(1+np.exp(-x))
    ### END CODE HERE ###

    return s

def sigmoid_derivative(x):
    """
    Compute the gradient (also called the slope or derivative) of the sigmoid function with respect to its input x.
    You can store the output of the sigmoid function into variables and then use it to calculate the gradient.
    
    Arguments:
    x -- A scalar or numpy array

    Return:
    ds -- Your computed gradient.
    """
    
    ### START CODE HERE ### (≈ 2 lines of code)
    s = basic_sigmoid(x)
    ds = s*(1-s)
    ### END CODE HERE ###
    
    return ds