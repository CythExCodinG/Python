#Abstract class is a class which hides the implementation details 
#ABC- Absract base class 
from abc import ABC,abstractmethod
class Friend(ABC):
  @abstractmethod
  def role(self):
    pass
class closefriend(Friend):
  def role(self):
    print("Rohit's Friends")

class wife(Friend):
  def role(self):
    print("Rohit Best Friend")

class RBI(ABC):
  @abstractmethod
  def roi(self,rate,inte):
    pass

class sbi(RBI):
  def roi(self,rate,inte):
    amt=rate*inte
    print("AMount will be:",amt)
class hdfc(RBI):
  def roi(self,rate,inte):
    amt=rate*inte
    print("Amt is :",inte)

sb1=sbi()
sb1.roi(12000,10)   
