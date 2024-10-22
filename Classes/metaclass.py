from abc import ABC,abstractmethod,ABCMeta
class emp(metaclass=ABCMeta):
  @abstractmethod
  def show(self):
    pass
  def display(self):
    print("My name is rohit and i am chu")

class employee(emp):
  def show(self):
    print("hello bhailog")
e1=employee()
e1.show()

class Student():
  def __init__(self):
    self.name="Rohit"
    self.age=23
stu1=Student()
print("Student name is :",stu1.name)
print(dir(stu1))

