'''
Ques 1: Write a Python program to create a list of size N and store the random values in it and find the sum
and average.
'''

from random import randrange as rr

def sum_avg(n):
    random_list=[]
    for i in range(n):
        random_list.append(rr(1, 101))
    total_sum = sum(random_list)
    average = total_sum / n 
    return random_list, total_sum, average

N = int(input("Enter the size of the list (N): "))
print(sum_avg(N))

# print(f"Random List: {random_list}")
# print(f"Sum: {total_sum}")
# print(f"Average: {average}")