import numpy as np 
  
a = np.array([0.0, 10.0, 20.0, 30.0]) 
b = np.array([0.0, 1.0, 2.0]) 
  
print(a[:, np.newaxis] + b) , "\n"

a = np.array([1.0,2.0,3.0])
b = 2.0
print(a * b) , "\n"

c = [2.0, 2.0, 2.0]
print(a * c) , "\n"
