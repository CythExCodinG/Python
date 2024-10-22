

from typing import Any


def add(a,b):
  print(a+b)
add(5,10)
add.__call__(50,100)
#__call__ inside the class

class demo:
  def __init__(self):
    print("constructer")
  def __call__(self):
    print("called")
d=demo()
d()
#Encapsulation means binding functions and variable into single unit
class student:
  def __init__(self,id,name):
    self.id=id
    self.name=name
  def __call__(self,college):
    print(self.id,self.name)
    print("College",{college})
  
s1=student(12,"Rohit")
s1("Rohit")

# class emp:
#   def __init__(self,name):
#     self.name=name
#   def show(self):
#     print(self.name)
# class dept(emp):
#   def __init__(self, name):
#     emp.__init__(self,name)
# d=dept("MCA")
# dept.show()

class emp:
  def __init__(self):
    print("Emp class")

class dept:
  def __init__(self):
    print("Dept class")
class dat(emp,dept):
  def __init__(self):
    emp.__init__(self)
    dept.__init__(self)

d1=dat()
