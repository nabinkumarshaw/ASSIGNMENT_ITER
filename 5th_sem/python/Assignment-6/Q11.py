'''Q11 Given the following two-dimensional arrays in NumPy: 
arrayl 
array2 
= 
= 
np.array([[0,1] ,[2,3]])
np.array([[4, 5],[6,7]])
Perform the following tasks:
(a) Use vertical stacking to create a 4-by-2 array named array3, with array1 stacked on top of 
array2?
(b) Use horizontal stacking to create a 2-by-4 array named array4, with array2 to the right of 
arrayl.
(c) Use vertical stacking with two copies of array4 to create a 4-by-4 array named array5. 
(d) Use horizontal stacking with two copies of array3 to create a 4-by-4 array named array6.
'''

import numpy as np

# Define the given arrays
array1 = np.array([[0, 1], [2, 3]])
array2 = np.array([[4, 5], [6, 7]])

# (a) Use vertical stacking to create a 4-by-2 array named array3
array3 = np.vstack((array1, array2))
print("Array3 (Vertical Stacking):")
print(array3)

# (b) Use horizontal stacking to create a 2-by-4 array named array4
array4 = np.hstack((array1, array2))
print("\nArray4 (Horizontal Stacking):")
print(array4)

# (c) Use vertical stacking with two copies of array4 to create a 4-by-4 array named array5
array5 = np.vstack((array4, array4))
print("\nArray5 (Vertical Stacking of Array4):")
print(array5)

# (d) Use horizontal stacking with two copies of array3 to create a 4-by-4 array named array6
array6 = np.hstack((array3, array3))
print("\nArray6 (Horizontal Stacking of Array3):")
print(array6)

 
 
 