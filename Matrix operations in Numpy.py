import numpy as np

A = np.array([[1,2,3],
              [4,5,6],
              [7,8,10]])

# Matrix Operations
print 'Rank of A:', np.linalg.matrix_rank(A)
print 'Trace of A:', np.trace(A)
print 'Determinant of A:', np.linalg.det(A)
print 'Inverse of A:\n', np.linalg.inv(A)
print 'Matrix raised to power of 3:\n', np.linalg.matrix_power(A,3)

# Solving linear equation set using linalg.solve
# Equations are:
# x + 2y = 8
# 3x + 4y = 18
# coefficients
a = np.array([[1,2],[3,4]])
# constants
b = np.array([8,18])
print 'Solution of the linear equation is: ', np.linalg.solve(a,b)
