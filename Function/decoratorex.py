#imp
def decor(func):
  def inner(x,y):
    if x<0:
      x=0
    if y<0:
      y=0
    return func(x,y)
  return inner

@decor
def add(a,b):
  return(a+b)
a=add(-20,40)
print("Addition is :",a)

@decor
def sub(a,b):
  return(a-b)
b=sub(-20,50)
print("Subtraction is :",b)


for i in range(1,201):
  print(i)