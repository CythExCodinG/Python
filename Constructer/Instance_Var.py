class emp:
  company="Yashmit"   # Class Variable
  def __init__(self,name,sal):
    self.name=name
    self.sal=sal
  def show(self):
    print(self.name,self.sal)
  def display():
    print(emp.company)
  @classmethod   # Class method must be made using decorator @classmethod 
  def display2(cls):
    print(cls.company+" 3")

e1=emp("rohit",2400)
e1.show()
print(e1.company)
print(emp.company) # Class Variable can be called with class name
# emp.display()
e1.display2()







