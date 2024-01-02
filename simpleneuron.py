import numpy as np 
import matplotlib.pyplot as plt 
import tensorflow as tf 
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras import Sequential
from tensorflow.keras.losses import MeanSquaredError, BinaryCrossentropy
from tensorflow.keras.activations import sigmoid   
X_train = np.array([[1.0], [2.0]], dtype=np.float32)           #(size in 1000 square feet)
Y_train = np.array([[300.0], [500.0]], dtype=np.float32)       #(price in 1000s of dollars)
#remember that my function was prediction(x)  = wx + b 
#so the weights are w and b FOR the neuron 
#neuron intailization 
linear_layer = tf.keras.layers.Dense(units=1 , activation="linear")  
linear_layer.get_weights() 
print(linear_layer.get_weights()) 
#no weights  so far so we need to train the neuron 
#training the neuron 
a1 = linear_layer(X_train[0].reshape(1,1))#NOW WE PASSED ONE OF THE DATA SET INPUTS , NOTE  THAT WE NEED TO PASS IT IN THE FORM OF A MATRIX SO WE RESHAPE IT 
print(f"prediction for the first data set input {a1}")  
#this neuron gave prediction on a random w and b now we need to set our weigths 
#setting the weights 
w = np.array([[100.0]], dtype=np.float32) 
b = np.array([200.0], dtype=np.float32) 
linear_layer.set_weights([w, b]) 
print(f"set weights as {linear_layer.get_weights()}")  
#lets predict on x again 
a1 = linear_layer(X_train[0].reshape(1,1)) 
print(f"prediction for the first data set input {a1}") 
#and lets predict by simply multiplying the weights with the input + b 
aIN = np.matmul(X_train[0], w) + b 
print(f"prediction for the first data set input {aIN}")  
