class A:
  def __init__(self,a,b):
    self.a=a
    self.b=b
  def add(self):
    return(self.a+self.b)
 
# Python can return multiple values

class add_sub:
  def __init__(self,a,b):
    self.x=a
    self.y=b 
  def __add__(self,other):
    m1=self.x+other.x
    m2=self.y+other.y
    return(m1,m2)
  def __add__(self,other):
    m1=self.x+other.x
    m2=self.y+other.y
    return(m1,m2)
  def __sub__(self,other):
    m1=self.x-other.x
    m2=self.y-other.y
    return(m1,m2)
a1=add_sub(20,80)
a2=add_sub(10,40)
a4=a1-a2
print(a4)

