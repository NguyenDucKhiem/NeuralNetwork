# import os libraly
import os
# set flag additionall filter out WARNING
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# import tensorflow libraly
import tensorflow as tf
# import models in keras
from keras.models import Sequential, Model
# import layers in keras
from keras.layers import Dense, Activation, Dropout, Input, LSTM
# import optimizers in keras
from keras import optimizers
# import numpy libraly
import numpy as np
# import csv libraly
import csv
# Split the data into Trainning and Test case
from sklearn.model_selection import train_test_split

# -----------------------------------------
# size val and test is 20% data
test_size = 0.2
# size val is 60% size val and test
val_size = 0.6
# seed
random_state = 1997
# -----------------------------------------
# you need to normalize values to prevent under/overflows.
def normalize(matrix, mean, std):
    '''
    Batch normalize\n

    matrix - matrix want to batch normalize\n
    mean - mean of matrix\n
    std - unit variance of matrix\n

    return normalize matrix
    '''

    # return
    return (matrix - mean) / std

# load data
train = np.loadtxt('dataset/data.csv', delimiter=',')
# spilit X
train_data, val_data = train_test_split(train[:,0:4], test_size=test_size, random_state=random_state)
# spilit Y
train_patient, val_patient = train_test_split(train[:,4:5], test_size=test_size, random_state=random_state)


# define mean X
mean_data = train_data.mean()
# define std X
std_data = train_data.std()
# define mean Y
mean_patient = train_patient.mean()
# define mean Y
std_patient = train_patient.max() - train_patient.min()

# normalize train X
train_data_norm = normalize(train_data, mean_data, std_data)
# normalize train Y
train_patient_norm = normalize(train_patient, mean_patient, std_patient)

# normalize val X
val_data_norm = normalize(val_data, mean_data, std_data)
# normalize val Y
val_patient_norm = normalize(val_patient, mean_patient, std_patient)

# spilit test
test_data_norm, val_data_norm, test_patient_norm, val_patient_norm = train_test_split(val_data_norm, 
        val_patient_norm, test_size=val_size, random_state=random_state)
# Input layer
data_inputs = Input(shape=(4,), name='data')

# Hiden layer
# layer 1
layer = Dense(5, activation='tanh', name='layer')(data_inputs)
# layer 2
layer = Dense(5, activation='tanh', name='layer_2')(layer)
# dropout layer
layer = Dropout(0.5)(layer)
# layer 3
layer = Dense(5, activation='tanh', name='layer_3')(layer)
# layer 4
layer = Dense(3, activation='tanh', name='layer_4')(layer)
# dropout layer
layer = Dropout(0.5)(layer)

# output layer
outputs = Dense(1, activation='tanh', name='layer_output')(layer)

# model have inputs is data_inputs and outputs is output
model = Model(inputs=data_inputs, outputs=outputs)

# prints a summary representation of a model
model.summary()
# optimizer adam, learning rate: 0.0001
adam = optimizers.Adam(lr=0.0001)
# compile with loss is mean squanred error and optimizer is adam
model.compile(loss='mean_squared_error', optimizer=adam) 

# import EarlyStopping, TensorBoard, CSVLogger in keras callbacks
from keras.callbacks import EarlyStopping, TensorBoard, CSVLogger

# create earlystopping callbacks with monitor val_loss, patence 5 epochs, moder max
my_callbacks = [EarlyStopping(monitor='val_loss', patience=5), 
                    # create tensorboard in ./seed_*/log
                    TensorBoard(log_dir='./seed_{}/logs'.format(random_state)),
                    # create file log csv in ./seed_*/logger.csv
                    CSVLogger('./seed_{}/logger.csv'.format(random_state), separator=',', append=False)]

#   Fit/train the model
history = model.fit(train_data_norm, train_patient_norm, epochs=1000, verbose=2, callbacks=my_callbacks,
    validation_data=[val_data_norm, val_patient_norm])

# fit test
score = model.evaluate(test_data_norm, test_patient_norm)

# log configuration of the model
with open('./seed_{}/log.txt'.format(random_state), 'a') as file:
    # write seperate logs to file
    file.write("************************************\n")
    # write shape data to file
    file.write("Shape data      :   {0}\n".format(train_data_norm.shape[0]))
    # write shape val to file
    file.write("Shape val       :   {0}\n".format(val_data_norm.shape[0]))
    # write shape test to file
    file.write("Shape test      :   {0}\n".format(test_data_norm.shape[0]))
    # write seed to file
    file.write("Random state    :   {0}\n".format(random_state))
    # write loss to file
    file.write("Loss on test    :   {0}\n".format(score))

# result data after training
ret = model.predict(normalize(train[:,0:4], mean_data, std_data)) * std_patient + mean_patient
# appent ret into data train
train = np.append(train, ret, axis=1)

# write result to result.csv
with open('./seed_{}/result.csv'.format(random_state), 'w') as data_file:
    # write 5 columns 'year', 'week', 'psi', 'rain', 'patient', 'result'
    write = csv.DictWriter(data_file, fieldnames=['year', 'week', 'psi', 'rain', 'patient', 'result'])
    # write header
    write.writeheader()
    # for each row of data train
    for data in train:
        # write row to file
        write.writerow({'year': data[0], 'week': data[1], 'psi': data[2], 
            'rain': data[3], 'patient': data[4], 'result': data[5]})
