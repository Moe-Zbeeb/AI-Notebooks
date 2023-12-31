import numpy as np 
import matplotlib.pyplot as plt 
x = np.array([1,2])  
y = np.array([300,500])  
print(f"my x is {x} andf my y is {y}")  
print(f"x.shape:{x.shape} and y.shape:{y.shape}")  
m = x.shape[0]  
print(f"traning examples : {m}")  
#in numpy the .shape return a tuple of the dimension of the array 
#so x.shape[0] is the first dimension of the array its a one dimensional array so it will return 1 number 
#but if it was a 2d array then it will return 2 numbers basically a python tuple  
#so m is the number of training examples
def computation(x,w,b):  
    return np.dot(x,w)+b  
#this function returns a vector of linear regression y's 
#the np.dot is the dot product of two arrays 
#lets now compute the linear regression data line and plot it 
line = computation(x,200,100)   
plt.plot(x,line,color='blue',label='linear regression line')  
plt.scatter(x,y,marker="x",color='red',label='data points')   
plt.title('linear regression')  
plt.xlabel('size')   
plt.ylabel('price') 
plt.legend() 
plt.show()   
#basically this is and exaaclty fitting line we call this overfitting 
#now lets predict a value 
size = 2.5 
price = computation(size,200,100)  
print(price)
