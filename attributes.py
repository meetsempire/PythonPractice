import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)

# b stores the number of dimensions of the array (2D or 3D)
b = a.ndim
print("Number of dimensions:", b)

# c stores the shape of the array (rows, columns)
c = a.shape
print("Shape (rows, columns):", c)

# d stores the item size (number of bytes for each element)
d = a.itemsize
print("Item size in bytes:", d)

# e stores the data type of the elements in the array
e = a.dtype
print("Data type:", e)

# f stores the total number of elements in the array
f = a.size
print("Total number of elements:", f)
