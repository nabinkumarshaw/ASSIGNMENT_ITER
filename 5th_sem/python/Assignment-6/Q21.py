'''Q21 Convert L=["Cry,, *Apple,, Orange,, 'Sky', 'Banana'] to a pandas series. Create a new series with 
the elements which has a vowel. Create another series which starts with a vowel. '''

import pandas as pd

# Original list
L = ["Cry", "Apple", "Orange", "Sky", "Banana"]

# Convert the list to a Pandas series
series = pd.Series(L)

# Create a new series with elements that contain at least one vowel
vowels = ['A', 'E', 'I', 'O', 'U']
contains_vowel_series = series[series.str.contains('|'.join(vowels), case=False)]

# Create a new series with elements that start with a vowel
starts_with_vowel_series = series[series.str[0].isin(vowels)]

print("Original Series:\n", series)
print("\nSeries with elements containing a vowel:\n", contains_vowel_series)
print("\nSeries with elements starting with a vowel:\n", starts_with_vowel_series)
