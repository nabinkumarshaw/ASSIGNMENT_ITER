'''
Ques 8: Write a function that takes n as an input and creates a list of n lists such that ith list contains the first
five multiples of i.
'''

def generate_multiples(n):
    result = [[i * j for j in range(1, 6)] for i in range(1, n + 1)]
    return result

# Input
n = int(input("Enter the value of n: "))
output = generate_multiples(n)

# Output
print("Generated list of multiples:")
for i, sublist in enumerate(output, start=1):
    print(f"Multiples of {i}: {sublist}")
