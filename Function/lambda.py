from functools import reduce
def mul(a):
  c=a*a
  return c
print("Square of no is :",mul(10))

#Lamda funtion also called as anonymous funtion
d=lambda x: x**2
print("Square of no 3 is :",d(3))

f=lambda a,b : 2*a*b
print(f(5,2))

list1=[3,2,6,8,4,6,2,9]
def even(a):
  l2=[]
  for i in a:
    if(i%2==0):
      l2.append(i)
  return l2
a=even(list1)
print(a)

#Filter first parameter is fun and second is sequence
#Filter allows you to extract values from seq given based on given condition

even_no=filter(lambda n : n%2==0,list1)
print(list(even_no))

#Map can be used to manipulate the filtered data set
even_no=[2,4,6,2,6,8]
twotime=list(map(lambda x: x*2,even_no))
print(twotime)

double=list(twotime)
sum=reduce(lambda x,y:x+y,double)
print("Sum of list is :",sum)
