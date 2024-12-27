'''Q8. Use linspace to create a 2x3 array with values from 1.1 to 6.6 and convert it to integers.'''

import numpy as np

array =np.linspace(1.1,6.6,6).reshape(2,3)

print(array)

int_array = array.astype(int)

print(int_array)