'''
Ques 2: Write a program to enter names and percentage of marks in a dictionary and display the information
on the screen.
'''

students = {}
n = int(input("Enter number of students: "))
for _ in range(n):
    name = input("Enter student name: ")
    percentage = float(input("Enter percentage: "))
    students[name] = percentage
print("Student Information:")
for name, percentage in students.items():
    print(f"{name}: {percentage}%")

