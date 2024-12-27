'''Q18 Write a Pandas program to convert the first column of a DataFrame as a Series. '''

import pandas as pd

# Create a sample DataFrame
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
}
df = pd.DataFrame(data)

# Convert the first column into a Series
first_column_series = df.iloc[:, 0]

print("Original DataFrame:\n", df)
print("\nFirst Column as Series:\n", first_column_series)
