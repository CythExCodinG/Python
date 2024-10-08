a=10
def outerfun():
  def innerfun():
    a=777
    print(a)
  innerfun()  #Scope of inner funtion in only inside outerfunction
outerfun()

def out():
  a="local"
  def inn():
    nonlocal a
    a="inner" #non local allow to modify a variable from the outer funtion within the nested funtion still its not a global variable
    print(a)
  print(a)
  inn()
out()

c=1
def add():
  global c
  c=c+2  #Global variable cannot be modified but we can change the value
  print(c)
add()

def fact(n):
  if(n==1):
    return n
  N
fact(6)
