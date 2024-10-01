l1=[2,5,4,6]
l2=[2,5,4,6]
print(id(l1)," ",id(l2))
#list behaves as an object 
print(l1==l2)
l3=[3,2,2,4,[2,4,5,6]]
print(id(l3[4][0]),id(l3[1]))
print("list 3 address :",id(l3),"Id of nested list :",id(l3[4]))