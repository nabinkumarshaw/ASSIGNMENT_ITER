'''Q16 Write a NumPy program to create a 9*9*2 array with random values and extract any array of shape 
(5,5,2) from the said array. '''

import numpy as np

# Create a 9x9x2 array with random values
array = np.random.random((9, 9, 2))

# Extract a 5x5x2 array from the 9x9x2 array
# Define starting row and column for the extraction (e.g., starting at index (2, 2))
start_row, start_col = 2, 2
extracted_array = array[start_row:start_row+5, start_col:start_col+5, :]

print("Original Array (9x9x2):\n", array)
print("\nExtracted Array (5x5x2):\n", extracted_array)
