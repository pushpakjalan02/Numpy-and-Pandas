import numpy as np

arr = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])

# Slicing operation
arr_sliced = arr[0:3:2, 0:4:3]
print "Sliced array is:\n", arr_sliced

# Integer array Indexing example
indexed_array = arr[[1,0,2],[3,0,1]]
print "\nThe indexed array is:\n", indexed_array

# Boolean array indexing example
cond = arr > 11
# cond is a boolean array
arr_boolean = arr[cond]
print "\nElements using boolean array indexing is:\n", arr_boolean
print "\nThe variable cond is:\n", cond
