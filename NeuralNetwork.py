import Math
import numpy as np

class NeuralNetwork:
    def __init__(self, X, Y, numberLayer):
        '''
        Init class
        
        Arguments:
        X -- data of size
        Y -- 
        w -- weights, a numpy array of size
        b -- bias, a scalar
        '''
        self.X = X
        self.Y = Y
        self.Z = {}
        self.W = {}
        self.B = {}
        self.numberLayer = numberLayer

    # GRADED FUNCTION: Set
    def Set(self, W, B, layer):
        '''
        Set dictionaries w, b in key = layer
        Arguments:
        w -- weights, a numpy array of size
        b -- bias, a scalar
        '''
        self.W[layer] = W
        self.B[layer] = B
    # END FUNCTION

    # GRADED FUNCTION: Forward
    def Forward(self, A_pre, g, layer):
        '''
        Forward propagation for layer

        Arguments:
        A_pre -- A[layer - 1]
        g -- activation function
        layer -- layer neural network
        
        Return:
        A -- A[layer]
        z
        '''
        self.Z[layer] = np.dot(self.W[layer], A_pre) + self.B[layer]
        A = g(self.Z[layer])

        return A
    # END FUNCTION: Forward

    # GRADED FUNCTION: Backward
    def Backward(self, dA, g, layer):
        '''
        Backward propagation for layer

        Arguments:
        dA -- da[layer]
        g -- gradient activation function

        Return:
        dA_pre -- da[layer - 1]
        dW
        dB
        '''
        m = self.X.shape[1] # number of examples

        dZ = dA * g(self.Z[layer])
        dA_pre = np.dot(self.W[layer].T, dZ)
        dW = np.dot(dZ, dA.T) * 1. / m 
        dB = np.sum(dZ, axis=1, keepdims=True) * 1. / m

        return {"dA" : dA_pre, "dW" : dW, "dB" : dB}
    # END FUNCTION: Backward

    # GRADED FUNCTION: propagate
    def propagate(self,w, b, g):
        """
        Implement the cost function and its gradient for the propagation explained above

        Arguments:
        w -- weights, a numpy array of size (num_px * num_px * 3, 1)
        b -- bias, a scalar
        g -- activation function

        Return:
        cost -- negative log-likelihood cost for logistic regression
        dw -- gradient of the loss with respect to w, thus same shape as w
        db -- gradient of the loss with respect to b, thus same shape as b
        
        Tips:
        - Write your code step by step for the propagation. np.log(), np.dot()
        """
        
        m = self.X.shape[1] # number of examples
        
        # FORWARD PROPAGATION (FROM X TO COST)
        ### START CODE HERE ### (≈ 2 lines of code)
        A = g(np.dot(w.T, self.X) + b)                                     # compute activation
        cost = np.sum(self.Y * np.log(A) + (1 - self.Y) * np.log(1 - A)) * 1. / (- m)                # compute cost
        ### END CODE HERE ###
        
        # BACKWARD PROPAGATION (TO FIND GRAD)
        ### START CODE HERE ### (≈ 2 lines of code)
        dw = np.dot(self.X, (A - self.Y).T) * 1. / m
        db = np.sum(A - self.Y) * 1. / m
        ### END CODE HERE ###

        assert(dw.shape == w.shape)
        assert(db.dtype == float)
        cost = np.squeeze(cost)
        assert(cost.shape == ())
        
        grads = {"dw": dw,
                "db": db}
        
        return grads, cost
    #end function

    # GRADED FUNCTION: optimize

    def optimize(self,w, b, g, gradient, num_iterations, learning_rate, print_cost = False):
        """
        This function optimizes w and b by running a gradient descent algorithm
        
        Arguments:
        w -- weights, a numpy array of size (num_px * num_px * 3, 1)
        b -- bias, a scalar
        g -- activation function
        gradient -- gradient activation function
        X -- data of shape (num_px * num_px * 3, number of examples)
        Y -- true "label" vector (containing 0 if non-cat, 1 if cat), of shape (1, number of examples)
        num_iterations -- number of iterations of the optimization loop
        learning_rate -- learning rate of the gradient descent update rule
        print_cost -- True to print the loss every 100 steps
        
        Returns:
        params -- dictionary containing the weights w and bias b
        grads -- dictionary containing the gradients of the weights and bias with respect to the cost function
        costs -- list of all the costs computed during the optimization, this will be used to plot the learning curve.
        
        Tips:
        You basically need to write down two steps and iterate through them:
            1) Calculate the cost and the gradient for the current parameters. Use propagate().
            2) Update the parameters using gradient descent rule for w and b.
        """
        
        costs = []
        
        for i in range(num_iterations):
            
            
            # Cost and gradient calculation (≈ 1-4 lines of code)
            ### START CODE HERE ### 
            grads, cost = self.propagate(w, b, g)
            ### END CODE HERE ###
            
            # Retrieve derivatives from grads
            dw = grads["dw"]
            db = grads["db"]
            
            # update rule (≈ 2 lines of code)
            ### START CODE HERE ###
            w = w - learning_rate * dw
            b = b - learning_rate * db
            ### END CODE HERE ###
            
            # Record the costs
            if i % 100 == 0:
                costs.append(cost)
            
            # Print the cost every 100 training examples
            if print_cost and i % 100 == 0:
                print ("Cost after iteration %i: %f" %(i, cost))
        
        params = {"w": w,
                "b": b}
        
        grads = {"dw": dw,
                "db": db}
        
        return params, grads, costs