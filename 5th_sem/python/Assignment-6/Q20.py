'''Q20 rite a Pandas program to find the index of the first occurrence of the smallest and largest value of a 
given series. If the input is [1,1, 3, 7,88, 12, 88, 23, 3, 1, 9, 0], the output should be 0 and 4.'''

import pandas as pd

# Create a Series
data = [1, 1, 3, 7, 88, 12, 88, 23, 3, 1, 9, 0]
series = pd.Series(data)

# Find the index of the first occurrence of the smallest value
min_index = series.idxmin()

# Find the index of the first occurrence of the largest value
max_index = series.idxmax()

print("Index of the smallest value:", min_index)
print("Index of the largest value:", max_index)
