'''Q14 Use the NumPy bincount function to count the number of occurrences of each non-negative integer 
in a 5-by-5 array of random integers in the range 0 — 99. '''

import numpy as np

# Generate a 5-by-5 array of random integers in the range 0-99
random_array = np.random.randint(0, 100, (5, 5))
print("Random Array:")
print(random_array)

# Flatten the array to a 1D array and use bincount to count occurrences
occurrences = np.bincount(random_array.flatten())

# Print the occurrences of each integer
print("\nOccurrences of each integer:")
for i in range(len(occurrences)):
    if occurrences[i] > 0:
        print(f"{i}: {occurrences[i]} times")
