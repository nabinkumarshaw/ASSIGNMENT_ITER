'''Q23 Perform the following tasks using the pandas DataFrame object: 
(a)Create a DataFrame named temperatures from a dictionary of three temperature readings 
each for *Maxine', *James', and *'Amanda'. 
(b)Recreate the DataFrame temperatures in Part (a) with custom indices using the index 
keyword argument and a list containing *"Morning', ' Afternoon', and "Evening'. 
(c)Select from temperatures the column of temperature readings for "Maxine'. 
(d)Select from temperatures the row of "Morning' temperature readings. 
(e)Select from temperatures the rows for "Morning' and "Evening' temperature readings. 
(f)Select from temperatures the columns of temperature readings for 'Amanda' and "Maxine'. 
(g)Select from temperatures the elements for 'Amanda' and *Maxine' in the "Morning” and 
*Afternoon'. 
(h)Use the describe method to produce temperatures' descriptive statistics. 
(i)Transpose temperatures. 
(j)Sort temperatures so that its column names are in alphabetical order

'''

import pandas as pd

# (a) Create a DataFrame named temperatures from a dictionary of temperature readings
data = {
    'Maxine': [23, 25, 22],
    'James': [21, 24, 20],
    'Amanda': [19, 21, 18]
}

temperatures = pd.DataFrame(data)
print("DataFrame (a):\n", temperatures)

# (b) Recreate the DataFrame with custom indices
temperatures_custom_index = pd.DataFrame(data, index=["Morning", "Afternoon", "Evening"])
print("\nDataFrame (b) - Custom Indices:\n", temperatures_custom_index)

# (c) Select the column of temperature readings for "Maxine"
maxine_temperatures = temperatures_custom_index['Maxine']
print("\nColumn for Maxine:\n", maxine_temperatures)

# (d) Select the row of "Morning" temperature readings
morning_temperatures = temperatures_custom_index.loc['Morning']
print("\nMorning Temperature Readings:\n", morning_temperatures)

# (e) Select the rows for "Morning" and "Evening" temperature readings
morning_evening_temperatures = temperatures_custom_index.loc[['Morning', 'Evening']]
print("\nMorning and Evening Temperature Readings:\n", morning_evening_temperatures)

# (f) Select the columns of temperature readings for 'Amanda' and 'Maxine'
amanda_maxine_temperatures = temperatures_custom_index[['Amanda', 'Maxine']]
print("\nColumns for Amanda and Maxine:\n", amanda_maxine_temperatures)

# (g) Select the elements for 'Amanda' and 'Maxine' in "Morning" and "Afternoon"
amanda_maxine_morning_afternoon = temperatures_custom_index.loc[['Morning', 'Afternoon'], ['Amanda', 'Maxine']]
print("\nAmanda and Maxine in Morning and Afternoon:\n", amanda_maxine_morning_afternoon)

# (h) Use the describe method to produce temperatures' descriptive statistics
descriptive_stats = temperatures_custom_index.describe()
print("\nDescriptive Statistics:\n", descriptive_stats)

# (i) Transpose temperatures
transposed_temperatures = temperatures_custom_index.T
print("\nTransposed DataFrame:\n", transposed_temperatures)

# (j) Sort temperatures so that its column names are in alphabetical order
sorted_temperatures = temperatures_custom_index.sort_index(axis=1)
print("\nSorted DataFrame by Column Names:\n", sorted_temperatures)
