'''Q9) Write a function format_2d_array (arr) that takes a two-dimensional array of positive integers 
(represented as nested lists) and returns a formatted string that mimics NumPy's column-based format. In be this format, each element in the array should be right-aligned, and the width of each column should 
determined by the number of characters required to display the largest element in the array. '''

def format_2d_array(arr):
    # Determine the maximum width of each column by finding the largest element in each column
    column_widths = [max(len(str(item)) for item in column) for column in zip(*arr)]
    
    # Format each row by aligning the elements based on the column widths
    formatted_rows = []
    for row in arr:
        formatted_row = "  ".join(f"{str(item):>{column_widths[i]}}" for i, item in enumerate(row))
        formatted_rows.append(formatted_row)
    
    # Join the rows into a single string with newlines between them
    return "\n".join(formatted_rows)

# Example usage:
arr = [
    [12, 345, 6],
    [789, 1, 2345],
    [56, 78, 9]
]

formatted_array = format_2d_array(arr)
print(formatted_array)
