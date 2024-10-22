class student:
  def __init__(self,name,rollno):
    self.__name=name
    self.__roll=rollno
  def show(self):
    print(self.__name)
s1=student("Rohit",23)
s1.show()
