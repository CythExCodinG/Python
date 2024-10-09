# *args variable length arguments
# *var_name creates a tuple 
def adder(*num):
  sum=0
  for i in num:
    sum+=i
  print(sum)
adder(2,3,4,2,5,6,3)
adder(10)


# *args allow to pass the number of variable of non keywords 
# to pass keywords as an arguments we can use **keywords
def intro(**data):
  for i,j in data.items():
    print(i,j)
intro(fname="rohit",lastname="bhalekar",age=30)

