import  numpy as np 
import matplotlib.pyplot as plt 
#data 
x = np.array([1,2])  
y = np.array([300,500])  
#basically cost function is the to the smmation of loss at every training example 
#we use least squared erros 
#loss = (y -   y_predicted)^2 
#1/m * sum(loss) over all m examples 

def loss (x,y,w,b) :  
   m = x.shape[0]  
   y_predicted = w*x + b 
   loss = np.sum((y - y_predicted)**2)/m 
   return loss     

