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

# Thu vien doc du lieu
import ReadFile

logPath = "./tb_logs/"

# Tao bieu do 
# FileWrite = tf.summary.FileWriter('file/graph', sess.graph)

# matrix lu tru doi tuong doc
matrix = np.transpose(ReadFile.Read())

# Plot generated 
# plt.plot(matrix[1:2], matrix[2:3], "bx")
# plt.ylabel("patient")
# plt.xlabel("weekly")
# plt.show()


# you need to normalize values to prevent under/overflows.
def normalize(matrix, mean, std):
    '''
    Cuan hoa du lieu dau vao
    '''
    return (matrix - mean) / std


# Split the data into Trainning and Test case
from sklearn.model_selection import train_test_split
test_size = 0.2
random_state = 52

train_data_week, test_data_week = train_test_split(matrix[1:4].T, test_size=test_size, random_state=random_state)
train_data_year, test_data_year = train_test_split(matrix[0:1].T, test_size=test_size, random_state=random_state)
train_data_patient, test_data_patient = train_test_split(matrix[3:4].T, test_size=test_size, random_state=random_state)

'''
# define mean and std
mean_week = train_data_week.mean()
std_week = train_data_week.std()
mean_year = train_data_year.mean()
std_year = train_data_year.std()
mean_patient = train_data_patient.mean()
std_patient = train_data_patient.std()

train_data_week_norm = normalize(train_data_week, mean_week, std_week)
train_data_year_norm = normalize(train_data_year, mean_year, std_year)
train_data_time_norm = np.append(train_data_week_norm, train_data_year_norm, axis=1)
train_data_patient_norm = normalize(train_data_patient, mean_year, std_patient)


test_data_week_norm = normalize(test_data_week, mean_week, std_week)
test_data_year_norm = normalize(test_data_year, mean_year, std_year)
test_data_time_norm = np.append(test_data_week_norm, test_data_year_norm, axis=1)
test_data_patient_norm = normalize(test_data_patient, mean_year, std_patient)
'''

# Input
week_inputs = Input(shape=(3,), name='week')
year_inputs = Input(shape=(1,), name='year')
# Hiden layer
layer = Dense(10, input_shape=(3,), activation='tanh', name='Week_Layer')(week_inputs)
# layer = Dense(6, activation='tanh', name='Week_Layer_2')(layer)
# layer = Dense(6, activation='tanh', name='Week_Layer_3')(layer)
layer = Dropout(0.5)(layer)

layer2 = Dense(2, input_shape=(3,), activation='tanh', name='Year_Layer')(year_inputs)
# layer2 = Dense(3, init='uniform', activation='tanh', name='Year_Layer_2')(layer2)
layer2= Dropout(0.5)(layer2)

con_layer = concatenate([layer, layer2])
con_layer = Dense(4, activation='tanh', name='Con_Layer')(con_layer)
con_layer = Dropout(0.5)(con_layer)
# Output
outputs = Dense(1, activation='linear', name='Layer_Output')(con_layer)

model = Model(inputs=[week_inputs, year_inputs], outputs=outputs)
model.summary()
sgd = optimizers.SGD(lr=0.01, decay=0.0, momentum=0.0, nesterov=False)
model.compile(loss='mean_squared_error', optimizer=sgd) # Loss and optimizer

from keras.utils import plot_model
from keras.callbacks import EarlyStopping

# plot_model(model, to_file='./logs/model.png', show_shapes=True, show_layer_names=True)
my_callbacks = [EarlyStopping(monitor='min_delta', patience=5, mode=max)]

#   Fit/train the model
history = model.fit([train_data_week, train_data_year], train_data_patient, nb_epoch=100, verbose=2, callbacks=my_callbacks)

# Note: fit cost values will be different because we did not use NN in original.
score = model.evaluate([test_data_week, test_data_year], test_data_patient)

file = open('./logs/log.txt', 'a')
file.write("************************************\n")
file.write("Test size       :   {0}\n".format(test_size))
file.write("Random state    :   {0}\n".format(random_state))
file.write("loss on test    :   {0}\n".format(score))
# print(history.)
print("\nloss on test : {0}".format(score))

# flag = 1
# while(flag):
#     year = input()
#     if year == 0:
#         break
#     month = input()
#     psi = input()
#     rain = input()
#     print(model.predict([year, month, psi, rain]))