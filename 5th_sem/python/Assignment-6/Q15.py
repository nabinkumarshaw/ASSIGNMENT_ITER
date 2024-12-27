'''Q15 Write functions median and mode that use existing NumPy capabilities to determine the median 
(middle) and mode (most frequent) of the values in an array. Your functions should determine the 
median and mode regardless of the array's shape. Test your function on three arrays of different 
shapes. '''

import numpy as np
from scipy.stats import mode

def median(array):
    """
    Calculate the median of the values in the array.

    Args:
        array (numpy.ndarray): Input array.

    Returns:
        float: Median value of the array.
    """
    return np.median(array)

def mode_function(array):
    """
    Calculate the mode of the values in the array.

    Args:
        array (numpy.ndarray): Input array.

    Returns:
        int: Mode value of the array.
    """
    flattened = array.flatten()
    mode_result = mode(flattened, axis=None, keepdims=False)
    return mode_result.mode

# Test the functions on three arrays of different shapes
array1 = np.array([1, 2, 2, 3, 4])
array2 = np.array([[10, 20, 20], [30, 40, 50]])
array3 = np.random.randint(1, 10, (4, 5))

print("Array 1:")
print(array1)
print("Median:", median(array1))
print("Mode:", mode_function(array1))

print("\nArray 2:")
print(array2)
print("Median:", median(array2))
print("Mode:", mode_function(array2))

print("\nArray 3:")
print(array3)
print("Median:", median(array3))
print("Mode:", mode_function(array3))
