class complexno:
  def __init__(self,real,img):
    self.img=img
    self.real=real

  def __add__(self,other):
    i1=self.img+other.img
    r1=self.real+other.real
    m=complexno(r1,i1)
    return m
  def __str__(self):
    return f"{self.real} +{self.img}i"

c1=complexno(20,30)
c2=complexno(30,40)
c3=c1+c2
print(c3.__str__())
 