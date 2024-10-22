#Python do not support method overloading
def add(a,b):
  return(a+b)
def add(a,b,c):
  return(a+b+c)

class addition:
  def add(self,a,b):
    return(a+b)
  def add(self,a,b,c,d):
    return(a+b+c+d)
  
class addition_one(addition):
  def add(self,a,b,c):    #Gives new difination to the funtion add() of parent class or super class
    return(a+b+c)
addi=addition_one()
print(addi.add(5,6,8))
