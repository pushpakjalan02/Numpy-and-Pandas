import numpy as np

arr1 = np.array([[1,2],[3,4]], dtype = np.float64)
arr2 = np.array([[5,6],[7,8]], dtype = np.float64)

# Additon of two arrays
Sum = np.add(arr1, arr2)
print "The sum of the two matrices is: \n", Sum

# Addition of all array elements using predefined sum method
Sum_of_elements = np.sum(arr1)
print "The sum of all elements of arr1 is:", Sum_of_elements

# Square root of array elements:
Sqrt = np.sqrt(arr1)
print "Square root of arr1 elements: \n", Sqrt

# Transpose of array using inbuilt function T
Trans_arr = arr1.T
print "Transpose of arr1: \n", Trans_arr
