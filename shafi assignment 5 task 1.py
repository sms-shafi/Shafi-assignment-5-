student_marks = {'shafi': 25,'deveen': 23,'kiran': 24,'abdul':22.5,'sukku':15}
name = input("Enter the student's name: ")
if name in student_marks:
   print(name+"'s marks: ",student_marks[name])
else:
   print('Student not found.')