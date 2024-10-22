# class Student:
#   def __init__(self):
#     self._name="Rohit"
#     self._age=23
  
# stu1=Student()
# print("Student name is :",stu1.name)
# print(dir(stu1))

class stu:
  def __init__(self):
    self._name="Rohit"
    self._age=23,

class exam(stu):
  def show(self):
    print("Student name is:",self._name)

class result(exam):
  def display(self):
    print("Student name is :",self._name)
res=result()
res.show()
res.display()

class student:
  _name="Sachin"
  _roll=34
  def __init__(self,name,rollno):
    self._name=name
    self._roll=rollno
  def _display(self):
    print(self._roll)

class mca(student):
  def displaydetail(self):
    self._display()
    
s=student("Rohit",23)
m=mca()
m.displaydetail()

