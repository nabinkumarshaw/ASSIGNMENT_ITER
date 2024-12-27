'''
Ques 7: Write a function that takes a list of numbers as input from the user and produces the corresponding
cumulative list where each element in the list at index i is the sum of elements at index j ≤ i.
'''


l=[2,4,1,5,7,3]
ans=[l[0]]
for i in range(1,len(l)):
    ans.append(ans[i-1]+l[i])
print(ans) 
# def cumulative_sum(numbers):
#     cumulative_list = []
#     total = 0
#     for num in numbers:
#         total += num
#         cumulative_list.append(total)
#     return cumulative_list

# numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
# result = cumulative_sum(numbers)
# print("Cumulative list:", result)