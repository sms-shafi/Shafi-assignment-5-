# ASSIGNMENT 5:
# Task 1: Create a Dictionary of Student Marks
---
# code: 

```
student_marks = {'shafi': 25,'deveen': 23,'kiran': 24,'abdul':22.5,'sukku':15}
# students marks are stored in dictionary 'student_marks'

name = input("Enter the student's name: ")
# this line takes the input from users and stores the content in variable called 'name'

if name in student_marks:
# 'if' block will run if the name 


   print(name+"'s marks: ",student_marks[name])


else:


   print('Student not found.')

