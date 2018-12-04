import NeuralNetwork as NN 
import ReadCSV

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
nn.Init()

for key in nn.W:
    print(nn.W[key])
    print()

#End Main