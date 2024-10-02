#method 1
print("############### Method 1 ###############")

l1=[2,5,4,7,8,3]
print("List before swapping",l1)
l1[0],l1[-1]=l1[-1],l1[0]
print("After Swapping",l1)

#method 2
print("############### Method 2 ###############")

l2=[4,5,2,6,8,3]
print("List before interchange",l2)
size=len(l2)
temp=l2[0]
l2[0]=l2[-1]
l2[-1]=temp
print("List After interchange",l2)

#Below when we assign multiple values to a var it creates a tuple
print("############### How unpacking works ###############")

n1=l1[0],l2[1]
n2=3,6,2,9,6
print(n1,type(n1),"\n",n2,type(n2))

#Method 3 using tuple unpacking swapping
print("############### Method 3 ###############")
l3=[3,5,2,9,8,5]
print("List Before interchange",l3)
tup1=l3[0],l3[-1]
l3[-1],l3[0]=tup1
print("List after interchange",l3)

#Method 4 using slicing
print("############### Method 4 ###############")
l4=[3,4,5,2,6,10]
print("List before Swapping :",l4)
l4=l4[-1:]+l4[1:-1]+l4[:1]
print("List After Interchange :",l4)




