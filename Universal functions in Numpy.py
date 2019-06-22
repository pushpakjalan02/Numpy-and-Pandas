import numpy as np

arr1 = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

# creation of array with sine values
arr_sine = np.array([0, np.pi/2, np.pi])
print "Sine Values are:\n", np.sin(arr_sine)

# creation of array with exponential values
arr_exp_sqrt = np.array([1,2,3,4])
print "Exponential Values are: \n", np.exp(arr_exp_sqrt)

# square root of array values
print "Square root Values are:\n", np.sqrt(arr_exp_sqrt)
