import math , copy 
import numpy as np 
import matplotlib.pyplot as plt 
X_train = np.array([[2104, 5, 1, 45], [1416, 3, 2, 40], [852, 2, 1, 35]])
y_train = np.array([460, 232, 178]) 
#the x now is the input its a matrix of col the train data fetures and the row is the n of the data  
#lets print some shape 
print(f"X_train shape is {X_train.shape} , and its type is {type(X_train)}")    
print(X_train)
print(f"y_train shape is {y_train.shape} , and its type is {type(y_train)}")  
#remember that now the w will a n vector  
#be will be a scalar 
b_init = 785.1811367994083
w_init = np.array([ 0.39133535, 18.75376741, -53.36032453, -26.42131618])
print(f"w_init shape: {w_init.shape}, b_init type: {type(b_init)}") 
#lets predict   
#for i in range (X_train.shape[0]):  # y_pred = x[i]*w[i]  
def compute(X_train,w_init,b_init): 
    y_pred = np.dot(X_train,w_init) + b_init 
    return y_pred 

def compute_cost(X_train,y_train,w_init,b_init): 
    y_pred = compute(X_train,w_init,b_init) 
    cost = np.sum((y_pred - y_train)**2) / (2*X_train.shape[0]) 
    return cost 
def compute_gradient(X_train,y_train,w_init,b_init): 
    y_pred = compute(X_train,w_init,b_init) 
    dw = np.dot(X_train.T ,  (y_pred - y_train)) / X_train.shape[0]  #this will return a vector of w n features 
    db = np.sum(y_pred - y_train) / X_train.shape[0] #this will return a scalar  
    return dw , db 
def update(X_train,y_train,w_init,b_init,learning_rate , iterartions): 
    w = copy.deepcopy(w_init) 
    b = copy.deepcopy(b_init) 
    for i in range (iterartions): 
        dw , db = compute_gradient(X_train,y_train,w,b) 
        w = w - learning_rate * dw 
        b = b - learning_rate * db 
        cost = compute_cost(X_train,y_train,w,b) 
        print(f"cost after {i} iterations is {cost}") 
        return w , b , cost