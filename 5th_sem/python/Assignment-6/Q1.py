'''Q1. Create a 2-by-3 array with ones, a 3-by-3 array with zeros, and a 2-by-5 array 
with sevens.'''

import numpy as np

array_ones = np.ones((2, 3))

array_zeros = np.zeros((3, 3))

array_sevens = np.full((2, 5), 7)

print("Array with ones:\n", array_ones)
print("\nArray with zeros:\n", array_zeros)
print("\nArray with sevens:\n", array_sevens)
