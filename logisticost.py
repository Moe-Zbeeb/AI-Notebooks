import math , copy 
import numpy as np   
X_train = np.array([[0.5, 1.5], [1,1], [1.5, 0.5], [3, 0.5], [2, 2], [1, 2.5]])
y_train = np.array([0, 0, 0, 1, 1, 1])
def sigmoidfunction(z) :
    return 1/(1+np.exp(-z))
 
def logisticcost(x,y,w,b) :  
        yhat = np.dot(x,w) + b 
        cost = 0 
        for i in range(x.shape[0]) :  
              sigmoid = sigmoidfunction(yhat[i])  
              cost += -y[i]*np.log(sigmoid)-(1-y[i])*(np.log(1-sigmoid))    
        return cost/x.shape[0]  

def compute_gradient_logistic(x,y,w,b) :  
        m = x.shape[0]   
        yhat = np.dot(x,w) + b  
        for i in range (m) :    
               yhat[i] = sigmoidfunction(yhat[i]) 
        dw = np.dot(x.T,(yhat-y))/m   
        db = np.sum(yhat-y)/m 
        return dw,db 
def compute_gradient_descent_logistic(x,y,w,b,learning_rate,iteration) : 
        w = copy.deepcopy(w) 
        b = copy.deepcopy(b) 
        for i in range(iteration) : 
              dw,db = compute_gradient_logistic(x,y,w,b) 
              w = w - learning_rate*dw 
              b = b - learning_rate*db 
        return w,b             
