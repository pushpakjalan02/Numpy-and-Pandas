import numpy as np

# Example creation of rank 1 array
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])

print "\nArray Creation of rank 2\n", arr1, "\n", arr2

print "Subracting from each array element\n", arr2 - 1
print "Adding from each array element\n", arr1 + 2
print "Summing each array element: ", arr1.sum()
print "Array addition:\n" , arr1 + arr2
