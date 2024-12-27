'''Q12 se NumPy's concatenate Function to reimplement the previous problem. '''

import numpy as np

# Define the given arrays
array1 = np.array([[0, 1], [2, 3]])
array2 = np.array([[4, 5], [6, 7]])

# (a) Use NumPy's concatenate to create a 4-by-2 array named array3 (Vertical stacking)
array3 = np.concatenate((array1, array2), axis=0)
print("Array3 (Vertical Concatenation):")
print(array3)

# (b) Use NumPy's concatenate to create a 2-by-4 array named array4 (Horizontal stacking)
array4 = np.concatenate((array1, array2), axis=1)
print("\nArray4 (Horizontal Concatenation):")
print(array4)

# (c) Use NumPy's concatenate with two copies of array4 to create a 4-by-4 array named array5
array5 = np.concatenate((array4, array4), axis=0)
print("\nArray5 (Vertical Concatenation of Array4):")
print(array5)

# (d) Use NumPy's concatenate with two copies of array3 to create a 4-by-4 array named array6
array6 = np.concatenate((array3, array3), axis=1)
print("\nArray6 (Horizontal Concatenation of Array3):")
print(array6)
