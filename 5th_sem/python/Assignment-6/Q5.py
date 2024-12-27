'''Q5. Create a 2x5 array from two lists of five prime numbers.'''

import numpy as np

list1 = [2, 3, 5, 7, 11]
list2 = [13, 17, 19, 23, 29]

arr = np.array([list1,list2])

print("2x5 Array of Primes:\n",arr)