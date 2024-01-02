import numpy as np
import tensorflow as tf  
X,Y = np.array([[0,0],[0,1],[1,0],[1,1]]), np.array([[0],[1],[1],[0]]) 
#lets normalize the data 
norm_l = tf.keras.layers.Normalization(axis=-1)
norm_l.adapt(X)  # learns mean, variance
Xn = norm_l(X) 
# lets build a sequential model forward propagation 
g =  sigmoid   

def mydense(ain , W , b ) :   
    units = W.shape[1] 
    aout = np.zeros(units)   
    for j in range(units) : 
        aout[j] = g(np.dot(ain,W[:,j])+b[j]) 
    return aout 
def my_sequential(X , W1 , b1 , W2 , b2) : 
    a1 = mydense(X , W1 , b1) 
    a2 = mydense(a1 , W2 , b2) 
    return a2  
def my_predict(X , W1 , b1 , W2 , b2) : 
    a2 = my_sequential(X , W1 , b1 , W2 , b2) 

