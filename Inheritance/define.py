# Inheritance is one word is Reuseability
class parent:
  def show(self):
    print("Parent")
class child(parent):
  def display(self):
    print("Child")
c1=child()
c1.show()
c1.display()

#Parent class Students
#Exams Sub AND Marks
#Results

class students:
  Name=""
  Rollno=0
  def __init__(self):
    Name=input("Enter Your Name :")
class exam(students):
  Sub1=""
  Sub2=""
  Sub3=""
  m1=0
  m2=0
  m3=0
  def __init__(self):
    super().__init__()
    exam.Sub1=input("Enter Your Sub1 :")
    print("Enter Your marks for that sub :")
    exam.m1=input(int())

    exam.Sub2=input("Enter Your Sub2 :")
    print("Enter Your marks for that sub :")
    exam.m2=input(int())

    exam.Sub3=input("Enter Your sub 3 :")
    print("Enter Your marks for that sub :")
    exam.m3=input(int())
class result(exam):
  avg=(super().m1+super().m2+super().m3)/3
  def __init__(self):
    super().__init__()
    print(result.avg)
r1=result()

    