#begin with importing the necessary libraries 
import numpy as np 
import matplotlib.pyplot as plt 
import tensorflow as tf  
import warnings 

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
def load_data():
    X = np.load("data/X.npy")
    y = np.load("data/y.npy")
    X = X[0:1000]
    y = y[0:1000]
    return X, y

def load_weights():
    w1 = np.load("data/w1.npy")
    b1 = np.load("data/b1.npy")
    w2 = np.load("data/w2.npy")
    b2 = np.load("data/b2.npy")
    return w1, b1, w2, b2  

def sigmoid(x):
    return 1. / (1. + np.exp(-x))   

#lests load the data and weights but after explaining the structure of the data 
#we want to recognise digits 0 or 1 written by hand 
#the data set is 1000 images of 20x20 pixels  
#we will transform the data into a 400x1 vector and stack them all in one matrix called X and Y is the data output this is a binary classification problem  SO Y WILL BE A 0 or 1  
X,y = load_data()  
#lets see the shape of the data and its values 
print(f"X shape is {X.shape} and y shape is {y.shape}") 

#lets see the first image 
print(f"the first image is {X[0]}")
####################################### 
#lets analyze the data 

warnings.simplefilter(action="ignore" , category=FutureWarning) 
m , n =  X.shape 
fig, axes = plt.subplots(8,8, figsize=(8,8))
fig.tight_layout(pad=0.1)

for i,ax in enumerate(axes.flat):
    # Select random indices
    random_index = np.random.randint(m) #here we selcted a random index from the data set
    
    # Select rows corresponding to the random indices and
    # reshape the image
    X_random_reshaped = X[random_index].reshape((20,20)).T #we mapped each row to a 20x20 matrix and transposed it to get the right orientation 
    #tranbspose is used to solve a common problem in image processing where the image is rotated by 90 degrees
    
    # Display the image
    ax.imshow(X_random_reshaped, cmap='gray')
    
    # Display the label above the image
    ax.set_title(y[random_index,0])
    ax.set_axis_off()  
plt.show() 

#let me explain the model we want to build 
#we have 400 input features and 1 output feature  
#we will use one input layer with 400 input mapped to first hidden layer with 25 neurons 
#then we will map the to second layer with 15 neurons and then to 
#the output layer with one neuron  
#x a1 a2 a3      
model = Sequential(
    [
        tf.keras.Input(shape=(400,)),    
        Dense(units=25, activation="sigmoid"),  
        Dense(units=15, activation="sigmoid"), 
        Dense(units=1, activation="sigmoid"), 
    ], name = "model"    
)
L1_num_params = 400 * 25 + 25  # W1 parameters  + b1 parameters
L2_num_params = 25 * 15 + 15   # W2 parameters  + b2 parameters
L3_num_params = 15 * 1 + 1     # W3 parameters  + b3 parameters
print("L1 params = ", L1_num_params, ", L2 params = ", L2_num_params, ",  L3 params = ", L3_num_params )   
[layer1, layer2, layer3] = model.layers

W1,b1 = layer1.get_weights()
W2,b2 = layer2.get_weights()
W3,b3 = layer3.get_weights()  
print(f"W1 shape = {W1.shape}, b1 shape = {b1.shape}")
print(f"W2 shape = {W2.shape}, b2 shape = {b2.shape}")
print(f"W3 shape = {W3.shape}, b3 shape = {b3.shape}") 

#run the loss function and gradient descent 
model.compile(
    loss=tf.keras.losses.BinaryCrossentropy(),
    optimizer=tf.keras.optimizers.Adam(0.001),
)

model.fit(
    X,y,
    epochs=20
) 
prediction = model.predict(X[0].reshape(1,400))  # a zero
print(f" predicting a zero: {prediction}")
prediction = model.predict(X[500].reshape(1,400))  # a one
print(f" predicting a one:  {prediction}") 

