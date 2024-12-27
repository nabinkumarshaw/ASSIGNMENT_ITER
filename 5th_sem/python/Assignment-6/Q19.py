'''Q19 Convert s1=[1,2,3,4,2] and s2=[3.4,5,6] to two series objects. Find elements in s1, which are not 
present in s2.'''

import pandas as pd

# Define the lists
s1 = [1, 2, 3, 4, 2]
s2 = [3.4, 5, 6]

# Convert the lists to Series objects
series1 = pd.Series(s1)
series2 = pd.Series(s2)

# Find elements in series1 that are not in series2
result = series1[~series1.isin(series2)]

print("Series 1:", series1)
print("Series 2:", series2)
print("\nElements in Series 1 that are not in Series 2:", result)
