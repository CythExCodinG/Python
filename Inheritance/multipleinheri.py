# In Case of Amibiguity it's solved Based of seq of inheritance (Method Resolution Order)
class p1:
  def show(self):
    print("My Name is P1")
class p2:
  def show(self):
    print("My Name is P2")
class child(p1,p2):
  pass
c1=child()
c1.show()

class Sbi:
  @classmethod
  def roi(cls,Rate,years):
    ratei=(Rate*years*7.5)/100
    return ratei
class HDFC:
  @classmethod
  def roi(cls,Rate,years):
    ratei=(Rate*years*8.5)/100
    return ratei
class fd(Sbi,HDFC):
  amt=input(int())
  yr=input(int())
  ratei=Sbi.roi(amt,yr)
  ratei2=HDFC.roi(amt,yr)
  print("Sbi :",ratei)
  print("Hdfc :",ratei2)
fixedD=fd()