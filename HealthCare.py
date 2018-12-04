import NeuralNetwork as NN 
import ReadCSV
import Math
import numpy as np

#Main
matrix = ReadCSV.Read(ReadCSV.WeeklyInfectiousFile)
# print(matrix.shape[0])
# print(matrix.shape[1])
# print(matrix[0:2])
# print(matrix[2:3])

nn = NN.NeuralNetwork(matrix[0:2], matrix[2:3], [3, 4, 5, 3])
# print(nn.X.shape)
# print(nn.Y.shape)
# print(len(nn.arrLayer))
nn.Init(10)
learning_rate = 0.01

# print(nn.W)

for count in range (0, 1000):
    A = nn.X
    for i in range(0, len(nn.arrLayer) + 1):
        # print(A[0][0])
        A = nn.Forward(A, Math.basic_sigmoid, i)

    dA = A - nn.Y
    mse = (np.square(A - nn.Y)).mean(axis=None)
    print ("MSE: ", mse)

    for i in range(len(nn.arrLayer), -1, -1):
        cache = nn.Backward(dA, Math.sigmoid_derivative, i)
        dA = cache["dA"]
        dW = cache["dW"]
        dB = cache["dB"]

        nn.W[i] = nn.W[i] - learning_rate * dW
        nn.B[i] = nn.B[i] - learning_rate * dB
        


#End Main