class MyException(Exception):    #Writing [Exception] keyword is important
  pass
def input_age():
  try:
    age=int(input("Enter Age :"))
    if age<0:
      raise MyException("Age Cannot be Negative")
  except MyException as E:
    print(E)
input_age()
#deligation Containership
#Regular expression -Pan Card no , PRN no  