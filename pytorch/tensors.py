"mentioning some tensors ops in torch"  
import torch 
import numpy as np 
"the empty"
x = torch.empty(2,3) 
print(x)  
"the random"   
x = torch.rand(2,4) 
"the zeros" 
x = torch.zeros(3,2) 
"the ones"  
x = torch.ones(3,2)   
print(x.dtype)   
x = torch.ones(2,2,dtype=torch.float32)  
print(x.size())  
x = torch.tensor([2.5,0.1])  


#operations  
x = torch.rand(2,2)  
y = torch.rand(2,2)  
z = x + y  
#or  
z = torch.add(x,y)  
#or inplace addition  
y.add_(x)  

#slicing 
print(x[:,0]) #first column all rows 
print(x[1,:]) #first row all cols 
print(x[1,1]) #get an element 
print(x[1:1].item()) #get the value in case of 1x1  
x = torch.rand(4,4) 
x = x.view(-1,8) #auto determine the write shape   


a = torch.ones(5)  
#converting to numpy 
b = a.numpy()  
a.add(1)  # ... 

c = torch.from_numpy(a) #also specify the datatypes 
#any change to np will change to torch if the tensor on GPU  

if torch.cuda.is_available():  
    device = torch.device("cuda")  
    y = torch.ones(5,device=device)  
    # to get to GPU 
    z = z.to(device)    

#when tensor is created  
x = torch.ones(5,requires_grad="True") 
