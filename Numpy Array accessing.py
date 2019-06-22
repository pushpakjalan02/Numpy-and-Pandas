import numpy as np

# Example creation of rank 1 array
arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print "\nArray Creation of rank 2\n", arr


# Printing range of elements in an array using slicing method
sliced_array = arr[:2,::2]
print "Sliced Array\n", sliced_array

# Printing elements at specific index of an array
index_array =arr[[1,2,2],[2,2,0]]
print "Elements at indices (1,2),(2,2),(2,0)", index_array
