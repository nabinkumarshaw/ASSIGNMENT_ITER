'''
Ques 11: Write a Python program to print M-by-N list in the tabular format.
'''

# m=3
# n=3
# for i in range(1,m+1):
#     for j in range(1,n+1):
#         print((i,j),end=" ")
#     print()  
    
def print_table(m, n):
    table = [[f"({i+1},{j+1})" for j in range(n)] for i in range(m)]
    
    for row in table:
        print("\t".join(str(cell) for cell in row))

m = int(input("Enter the number of rows (M): "))
n = int(input("Enter the number of columns (N): "))
print_table(m, n)