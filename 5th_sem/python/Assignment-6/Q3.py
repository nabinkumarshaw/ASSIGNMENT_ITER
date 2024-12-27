'''Q3. Create a 3x3 array of even integers (2 through 18). Create a second array with integers (9 down to 1). Multiply them.'''

import numpy as np

mat1 =np.arange(2,19,2).reshape(3,3)

print("Even Array:\n",mat1)

mat2 =np.arange(9,0,-1).reshape(3,3)

print("\nReversed Array:\n",mat2)

multiply =mat1 * mat2

print("\n Multiplication\n",multiply)