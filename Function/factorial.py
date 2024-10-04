def factorial(n):
  
  if(n<0):
    return "Factorial cannot be done"
  elif(n==1 or n==0):
    return "Factorial is : 1"
  else:
    fact=1
    for i in range(1,(n+1)):
      fact=fact*i
    return fact

n=int(input("Enter a no :"))
fact=factorial(n)
print(fact)
