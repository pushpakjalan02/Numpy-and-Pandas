# Python program for demonstrating the use of fields 

import numpy as np

# A structured datatype containing a 16-character string (in field 'name') and a sub-array
# of two 64-bit floating-point number (in field grades)

dt = np.dtype([('name', np.unicode_, 16),('grades', np.float64, (2,))])

print(dt['name'])
print(dt['grades'])

x = np.array([('Sara Lance', (8.2,7.9)),('John Diggle', (9.6, 8.4))], dtype = dt)

print x[0]
print x[1]
print "Grades of ", x[1]['name'], " are: ", x[1]['grades']
print "Names of students are: ", x['name']
