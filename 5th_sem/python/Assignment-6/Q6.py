'''Q6. Create a 2x3 array of powers of 2. Flatten it then ravel.In each case display the result then display 
the original array to show that it was unmodified.'''


import numpy as np

powers_of_2 = 2 ** np.arange(6).reshape(2, 3)

flattened = powers_of_2.flatten()

reshaped_ravel = powers_of_2.ravel()

print("Original Array:\n", powers_of_2)
print("\nFlattened Array:\n", flattened)
print("\nReshaped using Ravel:\n", reshaped_ravel)


# arr=2 ** np.arange(0,6).reshape(2,3)

# print(arr)

# # for item in arr.flat:
# #     print(item)
# print(arr.flatten())
    
#print(arr.ravel())

