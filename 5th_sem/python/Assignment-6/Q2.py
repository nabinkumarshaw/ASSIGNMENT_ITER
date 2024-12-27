'''Q2. Use arange to create a 2-by-2 array containing numbers 0-3. Perform the following operations:
(a) Cube every element of the array
(b) Add 7 to every element
(c) Multiply every element by 2'''

import numpy as np

np_arr =np.arange(4)
np_arr=np_arr.reshape(2,2)

cube =np_arr ** 3

add =np_arr + 7

mul =np_arr *2

print(np_arr)

print(cube)

print(add)

print(mul)


