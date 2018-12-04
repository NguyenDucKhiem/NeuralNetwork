import NeuralNetwork as NN 
import ReadCSV

#Main
matrix = ReadCSV.Read(ReadCSV.WeeklyInfectiousFile)
print(matrix.shape[0])
print(matrix.shape[1])

nn = NN.NeuralNetwork(matrix[0:1], matrix[2], [3, 4, 5, 3])
# for i : 


#End Main