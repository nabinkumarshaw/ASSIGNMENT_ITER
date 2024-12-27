'''Q17 Write a code to create a 4*4 array with random values and sort each column. '''

import numpy as np

# Create a 4x4 array with random values
array = np.random.random((4, 4))

# Sort each column
sorted_array = np.sort(array, axis=0)

print("Original Array (4x4):\n", array)
print("\nSorted Array (Columns Sorted):\n", sorted_array)
