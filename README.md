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
```
---
# Task 2: Demonstrate List Slicing 
---
# code:
```
numbers = list(range(1, 11))
# Creates a list 1 to 10

first_five_elements = numbers[:5]
# Extracts the first 5 elements: [1, 2, 3, 4, 5]

reverse_five_elements = first_five_elements.copy()
# Creates a copy so the original is unchanged

reverse_five_elements.reverse()
# Reverses the copied list

print('Original list:', numbers)
# print's  the full list

print('Extracted first five elements:', first_five_elements)
# print's the first five elements

print('Reversed extracted elements:', reverse_five_elements)
# reverses the extracted copy list
```
# Eample output:
```
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted first five elements: [1, 2, 3, 4, 5]
Reversed extracted elements: [5, 4, 3, 2, 1]

