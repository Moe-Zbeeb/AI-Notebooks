#begin with importing the necessary libraries 
import numpy as np 
import matplotlib.pyplot as plt 
import tensorflow as tf  
import warnings   
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
g = sigmoid 

def my_dense(ain , W , b , g) :   
    units = W.shape[1] 
    z = np.zeros(units) 
    for j in range (units) : 
        z[j]  = g(np.dot(ain , W[:,j]) + b[j])  
    return z  
def my_sequential(x,W1,b1,W2,b2,W3,b3) :  
    a1 = mydense(x,W1,b1,sigmoid)  
    a2 = mydense(a1,W2,b2,sigmoid)      
    a3 = mydense(a2,W3,b3,sigmoid) 
    return a3 
