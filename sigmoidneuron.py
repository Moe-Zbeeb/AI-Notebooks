import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras import Sequential
from tensorflow.keras.losses import MeanSquaredError, BinaryCrossentropy
from tensorflow.keras.activations import sigmoid  
 
X_train = np.array([0., 1, 2, 3, 4, 5], dtype=np.float32).reshape(-1,1)  # 2-D Matrix
Y_train = np.array([0,  0, 0, 1, 1, 1], dtype=np.float32).reshape(-1,1)  # 2-D Matrix

#sigmoid recap 
#sigmoid(z) = 1/(1+e^-z)  where e is the euler number and x is the wx+b 
#sigmoid(z) = 1/(1+e^-wx+b) z = wx+b 
#we need to activate as a sigmoid 
model = Sequential(
    [
        tf.keras.layers.Dense(1 , input_dim=1, activation="sigmoid", name="L1")
    ]
)

print(model.summary())  
logistic_layer = model.get_layer('L1')  
w,b = logistic_layer.get_weights() 
print(f"weights are {w} and bias is {b} and the shape of w is {w.shape} and the shape of b is {b.shape}")  
logistic_layer.set_weights([np.array([[2.0]]), np.array([-4.5])])  
print(f"the weights now are {logistic_layer.get_weights()}") 
#lets predict on the first data set input    '
a1 = logistic_layer(X_train[0].reshape(1,1)) 
print(f"prediction for the first data set input {a1}") 
#lets predict on the normal sigmoid 
ain = sigmoid(np.dot(X_train[0], np.array([[2]])) + np.array([-4.5]))    
print(f"prediction for the first data set input {ain}") 