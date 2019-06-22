import numpy as np

# Guessed Datatype
x = np.array([[1,2],[3,4]])
y = np.array([[1.0,2.0],[3.0,4.0]])

print("Array y is", y.dtype)
print("Array x is", x.dtype)

x = np.array([[1,2],[3,4]], dtype = np.int64)
print("Array x is", x.dtype)
