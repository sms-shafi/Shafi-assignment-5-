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
# 'if' block will run if the user input name found in 'student_marks'

   print(name+"'s marks: ",student_marks[name])
# it print's the student name marks provided by user 

else:
#thiis block will run if input was not found in 'student_marks'

   print('Student not found.')
# it print's student not found
```
# Example output:
```
Enter the student's name: shafi
shafi's marks:  25
