import numpy as np
#Slicing și view vs copy: array 1×10; slice 2..7; modifică slice-ul și verifică efectul asupra originalului.
x = np.array([1,2,3,4,5,6,7,8,9,10])
print("Array principal:", x)
#Slicing
x_slice = x[2:7]
print( "Slicing:", x_slice)

#View
x_view = x.view()
x_view_slice = x_view[2:7]
print("View", x_view_slice)
#Copy
x_copy = x.copy()
x_copy_slice = x_copy[2:7]
print("Copy:",x_copy_slice)
#Modificam Slice
print("----------------")
x_slice[0] = 100
print("Dupa Modificare",x_slice)
print("Original",x)
print("View",x_view_slice)
print("Copy",x_copy_slice)

