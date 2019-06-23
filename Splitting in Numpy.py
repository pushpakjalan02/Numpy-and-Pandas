import numpy as np

a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

# horizontal splitting
print "Splitting along horizontal axis:\n", np.hsplit(a,3)

# vertical splitting
print "Splitting along vertical axis into 2 parts", np.vsplit(a,3)
