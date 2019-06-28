import numpy as np

print(np.dtype(np.int16))

# Pyhton program to create a data type object containing 32-bit big-endian integer

# i4 represents integer of size 4 byte
# > represents big-endian byte ordering and < represents little-endian ordering
# dt is datatype object

dt = np.dtype('>i4')

print "Byte order is: ", dt.byteorder
print "Size is: ", dt.itemsize
print "Data type is: ", dt.name

# Proving dtype and type are different

a = np.array([1])

print "Type is: ", type(a)
print "dtype is: ", a.dtype
