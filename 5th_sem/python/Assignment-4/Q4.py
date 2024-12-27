'''
Ques 4: Write a Python program that removes all occurrences of a specific element from a list.
'''
# remove all 4 from this list

def remove_ele(l,ele):
    new_l=[x for x in l if x!=ele]
    return new_l
    
l=[2,4,3,4,3,4,3,5,4,6]
print(remove_ele(l,4))
