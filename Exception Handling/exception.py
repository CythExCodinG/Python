def div(a,b):
  c=0
  try:
    c=a/b
  except:
    print("Cannote divide by zero")
  return c
print(div(2,0))
#write code inside the try that code whose responsible for generating the reponse
#try and except => in except write those words that user can understand

def div(a,b):
  c=a/b
  print(c)
try:
  print(div(2,0))
except:
  print("Cannot divide by zero")

#If name of exception is known 
def div(a,b):
  c=a/b
  print(c)
try:
  list=[23,2,3,23]
  print(list[10])
  print(div(2,5))
except ZeroDivisionError:
  print("Cannot divide by zero man")
except:
  print("For all")

# if we use assert and the cond is true we can perfrom anything but if false then it will throw an error of assertion exception
num=0
try:
  num=int(input("Enter a no :"))
  assert num%2==0
except:
  print(num,"is not an even")
else:
  recp="1/num"
  print(recp)
finally:
  print("execution done")
#Finally block is always executed at the last 