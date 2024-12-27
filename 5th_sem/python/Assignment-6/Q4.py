'''Q4. Create a 2D array and swap the first two rows and columns.'''

import numpy as np

array = np.arange(1, 10).reshape(3, 3)

swapped_rows = array[[1, 0, 2], :]

swapped_columns = array[:, [1, 0, 2]]

print("Original Array:\n", array)
print("\nArray after swapping rows:\n", swapped_rows)
print("\nArray after swapping columns:\n", swapped_columns)

