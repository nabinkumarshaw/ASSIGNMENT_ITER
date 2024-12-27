'''Q13 Use NumPy's tile function to create a checkerboard pattern of dashes and asterisks '''

import numpy as np

# Use NumPy's tile function to create a checkerboard pattern of dashes and asterisks
checkerboard_pattern = np.tile([['-', '*'], ['*', '-']], (4, 4))

print("Checkerboard Pattern:")
print(checkerboard_pattern)
