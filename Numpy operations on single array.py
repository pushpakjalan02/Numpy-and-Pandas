import numpy as np

# Performing operations on single array
arr1 = np.array([1,2,3,4])

# Performing addition
print "Added array: \n", arr1+2, "\n"

# Performing subtraction
print "Subtracted array: \n", arr1-9, "\n"

# Performing multiplication
print "Multiplied array: \n", arr1*6, "\n"

# Performing cube
print "Cubed array: \n", arr1**3, "\n"

# Modifying original array
arr1 +=4
print "Modified array: \n", arr1, "\n"

# Transposed original array
arr2 = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
transposed_array = arr2.T
print "Transposed array: \n", transposed_array, "\n"
