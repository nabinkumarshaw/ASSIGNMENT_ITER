'''Q10. Create an array with values 1-15, reshape to 3x5, and then use indexing and slicing techniques to
perform each of the following operations
a)select row 2
b)select column 5
c)select row 0 and 1
d)select columns 2-4
e)select the elements that is in row 1 and column 4
f)select all elements from rows 1 and 2 that are in column 0,2,and 4'''

import numpy as np

arr =np.arange(1,16).reshape(3,5)
print(arr)

row_2 =arr[1,:]
print("\n",row_2)

col_5 =arr[:,4]
print("\n",col_5)

row_0_1=arr[[0,1],:]
#row_0_1 = arr[:2, :]
print("\n",row_0_1)

columns_2_to_4 = arr[:, 1:4]
print("\n",columns_2_to_4)

element_1_4 = arr[0, 3]
print("\nColumns 2-4:\n", columns_2_to_4)

subset = arr[1:, [0, 2, 4]]

print("\nElement at Row 1, Column 4:\n", element_1_4)


