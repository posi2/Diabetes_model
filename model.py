import numpy as np
import keras
import tensorflow as tf
from keras import backend as K
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json

K.clear_session()

def prediction(input_value):

    input_list = []
    for key, value in input_value.items():
        input_list.append(value)
    input_list = np.array(input_list)
    input_list = input_list.reshape( (1,8) )
    input_list = np.matrix(input_list)

    json_file = open('/home/posi2/Data-Science/pima-indians-diabetes-database/model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()

    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("/home/posi2/Data-Science/pima-indians-diabetes-database/model.h5")
    loaded_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    values=loaded_model.predict(input_list)
    return values
