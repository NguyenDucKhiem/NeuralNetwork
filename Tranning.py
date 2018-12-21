import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf 
import math
import numpy as np
# Thu vien mo rong 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from keras.models import Sequential, Model
from keras.layers import Dense, Activation, Dropout, Input
from keras.layers import concatenate
from keras import optimizers
# Trinh toi uu Adam
from keras.optimizers import Adam

# you need to normalize values to prevent under/overflows.
def normalize(matrix, mean, std):
    return (matrix - mean) / std


# Split the data into Trainning and Test case
from sklearn.model_selection import train_test_split
test_size = 0.2
random_state = 52

train = np.loadtxt('dataset/data.csv', delimiter=',')
train_data, val_data = train_test_split(train[:,0:4], test_size=test_size, random_state=random_state)
train_patient, val_patient = train_test_split(train[:,4:5], test_size=test_size, random_state=random_state)

# define mean and std
mean_data = train_data.mean()
std_data = train_data.std()

mean_patient = train_patient.mean()
std_patient = train_patient.max() - train_patient.min()

train_data_norm = normalize(train_data, mean_data, std_data)
train_patient_norm = normalize(train_patient, mean_patient, std_patient)


val_data_norm = normalize(val_data, mean_data, std_data)
val_patient_norm = normalize(val_patient, mean_patient, std_patient)

# Input
data_inputs = Input(shape=(4,), name='data')

# Hiden layer
layer = Dense(5, activation='tanh', name='layer')(data_inputs)
layer = Dense(5, activation='tanh', name='layer_2')(layer)
layer = Dense(5, activation='tanh', name='layer_3')(layer)
layer = Dense(3, activation='tanh', name='layer_4')(layer)
layer = Dropout(0.5)(layer)

outputs = Dense(1, activation='tanh', name='layer_output')(layer)

model = Model(inputs=data_inputs, outputs=outputs)
model.summary()
sgd = optimizers.SGD(lr=0.001, decay=0.0, momentum=0.0, nesterov=False)
model.compile(loss='mean_squared_error', optimizer=sgd) # Loss and optimizer

from keras.utils import plot_model
from keras.callbacks import EarlyStopping, TensorBoard, CSVLogger

my_callbacks = [EarlyStopping(monitor='val_loss', patience=5, mode=max), 
                    TensorBoard(log_dir='./seed_{}/logs'.format(random_state)),
                    CSVLogger('./seed_{}/logger.csv'.format(random_state), separator=',', append=False)]

#   Fit/train the model
history = model.fit(train_data_norm, train_patient_norm, nb_epoch=300, verbose=2, callbacks=my_callbacks,
    validation_data=[val_data_norm, val_patient_norm])

# Note: fit cost values will be different because we did not use NN in original.
score = model.evaluate(val_data_norm, val_patient_norm)

with open('./seed_{}/log.txt'.format(random_state), 'a') as file:
    file.write("************************************\n")
    file.write("Shape data      :   {0}\n".format(train_data_norm.shape[0]))
    file.write("Shape val       :   {0}\n".format(val_data_norm.shape[0]))
    file.write("Test size       :   {0}\n".format(test_size))
    file.write("Random state    :   {0}\n".format(random_state))
    file.write("Loss on test    :   {0}\n".format(score))

print("\nloss on test : {0}".format(score))

print("Do you want to test (y/n): ")
flag = input()
if flag == 'y' or flag == 'Y':
    while(True):
        print('year: ')
        year = int(input())
        if year == 0:
            break

        print('month: ')
        month = int(input())

        print('psi: ')
        psi = int(input())

        print('rain: ')
        rain = int(input())

        data = [[year, month, psi, rain]]
        data = normalize(data, mean_data, std_data)
        ret = model.predict(data) * std_patient + mean_patient
        print(ret)