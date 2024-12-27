'''
Ques 3: Design and develop a menu-driven Python program for the following list operations.
a. Create a list of N integers
b. Display the list elements
c. Insert an element at a specific position
d. Delete an element at a given position
e. Exit
'''

# from random import randrange as rr
# def insert(l):
#     for i in range(5):
#         l.append(rr(1,10))
#     return l
    
# def display(l):
#     for i in l:
#         print(i,end=" ")
        
# def insertat(ele,pos,l):
#     l.insert(pos,ele)
#     return l
    
# def delete(pos,l):
#     l.remove(l[pos])
    
# l=[]
# insert(l)
# display(l)
# print()
# insertat(100,2,l)
# display(l)
# print()
# delete(2,l)
# display(l)

def create_list(n):
    return [int(input(f"Enter element {i + 1}: ")) for i in range(n)]

def display_list(lst):
    print("List elements:", lst)

def insert_element(lst, element, position):
    if 0 <= position <= len(lst):
        lst.insert(position, element)
        print(f"Inserted {element} at position {position}")
    else:
        print("Invalid position!")

def delete_element(lst, position):
    if 0 <= position < len(lst):
        removed_element = lst.pop(position)
        print(f"Deleted element {removed_element} from position {position}")
    else:
        print("Invalid position!")


lst = []
while True:
    print("\nMenu:")
    print("1. Create a list of N integers")
    print("2. Display the list elements")
    print("3. Insert an element at a specific position")
    print("4. Delete an element at a given position")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
        
    if choice == 1:
        n = int(input("Enter the number of elements: "))
        lst = create_list(n)
    elif choice == 2:
        display_list(lst)
    elif choice == 3:
        element = int(input("Enter the element to insert: "))
        position = int(input("Enter the position to insert at: "))
        insert_element(lst, element, position)
    elif choice == 4:
        position = int(input("Enter the position to delete from: "))
        delete_element(lst, position)
    elif choice == 5:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice! Please select a valid option.")