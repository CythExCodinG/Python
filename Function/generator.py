#Generator generate sequence of values 
#it's iteraable
#Yeild returns the value
#imp
def greet():
  yield "hello"
  yield "Jod"
g=greet()
for i in g:
  print(i)

def m(x,y):
  while x<=y:
    yield x
    x+=1
g=m(3,10)
for i in g:
  print(i)
