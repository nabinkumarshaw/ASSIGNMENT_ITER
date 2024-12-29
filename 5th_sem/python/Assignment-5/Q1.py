'''Write aprogramtoaccept student name and marks fromthe user and create a dictionary. Also, display
 student marks by taking student name as input.'''
 
students = {}
for i in range(3):
    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))
    students[name] = marks
    
# print(students)
search_name = input("Enter the name to search: ")
if search_name in students.keys:
    print(f"marks of {search_name} is {students.get(search_name)}")
else:
    print("student not found")
