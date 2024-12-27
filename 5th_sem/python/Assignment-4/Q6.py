'''
Ques 6: Input 10 integers from the keyboard into a list. The number to be searched is entered through the
keyboard by the user. Write a Python program to find if the number to be searched is present in the
list and if it is present, display the number of times it appears in the list.
'''




def counting(l,search):
    count=0
    for i in l:
        if(i==search):
            count+=1
    return count
    
# l=[]
# for i in range(5):
#     num=int(input(f"enter {i+1} number in list\n"))
#     l.append(num)
# print(l)  
l=[1,2,4,3,4,4,6,7,1,3]
search=4
ans=counting(l,search)
print(f"Number of times {search} appear is {ans}")

# numbers = [int(input(f"Enter integer {i + 1}: ")) for i in range(10)]
# search_number = int(input("Enter the number to search: "))
# count = numbers.count(search_number)

# if count > 0:
#     print(f"The number {search_number} is present {count} time(s) in the list.")
# else:
#     print(f"The number {search_number} is not present in the list.")