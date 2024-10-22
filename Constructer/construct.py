# class Student:
#   def __init__(self):         latest defination given to contructer is filled 
#     print("Contructer")
#   def __init__(self):
#     print("Contructer 2")
# s1=Student()

class Student:
  def __init__(self):
    print("Contructer")
  def __del__(self):
    print("Destructor")
s1=Student()
s2=Student()
