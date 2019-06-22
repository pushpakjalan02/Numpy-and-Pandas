import numpy as np

arr = np.array([[1,2],
                [3,4],
                [5,6]])

# Maximum and minimum element of array

# Largest element in whole array
print "Largest element in the whole array is: ", arr.max(), "\n"
# Row-wise maximum element
print "Row-wise maximum of the whole array is: ", arr.max(axis = 1), "\n"
# Column-wise minimum element
print "Column-wise minimum of the whole array is: ", arr.min(axis = 0), "\n"

# Cumulative sum along each row
print "Cumulative sum along each row is: ", arr.cumsum(axis = 1), "\n"
