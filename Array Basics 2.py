import numpy as np

arr1 = np.array([[1,2,4],[5,8,7]], dtype = 'float')
print "Array created using passing list\n", arr1

arr2 = np.array(((1,2,3),(4,5,6)))
print "Array by passing tuple\n", arr2

# Creating 3X4 Array with all zeros
arr3 = np.zeros((3,4))
print "Array with all zeros is:\n", arr3

# Creating a constant value array of integer and complex type
arr4 = np.full((2,3), 6, dtype = np.int64)
arr5 = np.full((2,3), 6+2j, dtype = 'complex')
print "Array 4 is\n", arr4
print "Array 5 is\n", arr5

# Creating an array of random values
arr6 = np.random.random((2,2))
print "Array of random values:\n", arr6

# Creating an array of sequence of integers form 90 to 150 in steps of 2
arr7 = np.arange(90, 150, 2)
print "A sequential array of elements from 90 to 150 in steps of 2\n", arr7

# Creating a sequence of 100 values in range of 20 to 40.
arr8 = np.linspace(20,40,100)
print "Array with sequence of 100 vaues in between 20 to 40 is: \n", arr8

# Reshaping an array
arr9 = np.array([[1,2,3],[4,5,6]])
arr9_reshaped = arr9.reshape(2,1,3)
print "Original array:\n", arr9, "\nReshaped array:\n", arr9_reshaped

# Flattening an array
arr10 = np.array([[1,2],[3,4]])
arr10_flattened = arr10.flatten(order = 'C')
print "Flattened array\n", arr10_flattened
