import numpy as np


a = np.array([[1, 4, 2],
              [3, 4, 6], 
              [0, -1, 5]])

# Array Sorting 
print "\nArray elements in sorted order:\n", np.sort(a, axis = None)

# Row-wise sorting of array 
print "\nRow-wise sorted array:\n", np.sort(a, axis = 1)

# Specifying the sorting algorithm
print "\nColumn wise sort by applying merge-sort:\n", np.sort(a, axis = 0, kind = 'mergesort') 
  
# Example to show sorting of structured array 
# set alias names for dtypes 
dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)] 
  
# Values to be put in array 
values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7),  
           ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)] 
             
# Creating array 
arr = np.array(values, dtype = dtypes) 
print "\nArray sorted by names:\n", np.sort(arr, order = 'name') 

print "\nArray sorted by grauation year and then cgpa:\n", np.sort(arr, order = ['grad_year', 'cgpa'])
