'''Q22 Perform the following tasks using the pandas Series object: 
    
(a) Create a Series from the list [7, 11, 13, 17].
(b) Create a Series with five elements where each element is 100. 0.
(c) Create a Series with 20 elements that are all random numbers in the range 0 to 100. Use the 
describe method to produce the Series' basic descriptive statistics.
(d) Create a Series called temperatures with the following floating-point values: 98.6, 98.9, 
100.2, and 97.9. Use the index keyword argument to specify the custom indices Julie', 
'Charlie', 'Sam', and *Andrea'. 
(e)Form a dictionary from the names and values in Part (d), then use it to initialize a Series. 
'''

import pandas as pd
import numpy as np

# (a) Create a Series from the list [7, 11, 13, 17]
series_a = pd.Series([7, 11, 13, 17])
print("Series (a):\n", series_a)

# (b) Create a Series with five elements where each element is 100
series_b = pd.Series([100] * 5)
print("\nSeries (b):\n", series_b)

# (c) Create a Series with 20 elements that are all random numbers in the range 0 to 100
series_c = pd.Series(np.random.randint(0, 101, size=20))
print("\nSeries (c):\n", series_c)

# Use describe method to produce the Series’ basic descriptive statistics
print("\nDescriptive Statistics (c):\n", series_c.describe())

# (d) Create a Series called temperatures with the following floating-point values
temperatures = pd.Series([98.6, 98.9, 100.2, 97.9], index=['Julie', 'Charlie', 'Sam', 'Andrea'])
print("\nSeries (d) - Temperatures:\n", temperatures)

# (e) Form a dictionary from the names and values in Part (d), then use it to initialize a Series
temperature_dict = {'Julie': 98.6, 'Charlie': 98.9, 'Sam': 100.2, 'Andrea': 97.9}
series_e = pd.Series(temperature_dict)
print("\nSeries (e) - Using Dictionary:\n", series_e)
