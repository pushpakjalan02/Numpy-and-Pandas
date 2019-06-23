import numpy as np

arr1 = np.array([[1,2,3],
                [4,5,6]])
arr2 = np.array([[7,8,9],
                [10,11,12]])

# Vertical Stacking

print "Vertical stacking\n", np.vstack((arr1,arr2))

#Horizontal Stacking

print "Horizontal Stacking\n", np.hstack((arr1,arr2))

# Column Stacking

column_array_to_stack = [7,8]
print "Column Stacked output:\n", np.column_stack((arr1, column_array_to_stack))

# Concatenation method
print "\nConcatenation to 2nd axis:\n", np.concatenate((arr1,arr2),1)
print "\nConcatenation to 1st axis:\n", np.concatenate((arr1,arr2),0)
