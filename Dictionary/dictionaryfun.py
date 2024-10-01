student={'name':'Rohit','class':'FYMCA','elective':'Web Dev'}
for i in student:
  print(i)
print(student.values())
student['class']='Mca'
print(student)
student['dob']='06/07/2003'
print(student)
print(student.pop('class'))
print(student)
