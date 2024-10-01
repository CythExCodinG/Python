l1=[2,3,4,5,2,1]
print(type(l1))
l2=["rohit",2,3,"Rushabh"]
print(type(l2))
l3=[2]
print(type(l3))
list=[2,4,6,8,[2,5,7,8],63,9]
print(list[4][3])
print(list[2])
list[4][2]=22
print(list[::-2])
l1.insert(2,99)
print(l1)
l1.remove(5)
print(l1)
list2=[4,5,2,6,2,5,9]
list2.append(77)
print(list2)
list4=[3,5,7]

list5=[5,8,9]
list4.extend(list5)
list4.append(list5)
print(list4)
list5.reverse()

list5.pop()
print(list5)
print(list4)

list5=[3,6,8,4]
del(list5[2])
print(list5)


list5.clear()
print(list5)


list6=[3,4,2,5,7,6]
list7=list6[:]
print(list6,list7)
print(id(list6),id(list7))
list6[1]=10
print(list6,list7)
a=[2,3,4,2]
b=a
print(id(a),id(b))

#In shallow copy chages made in other refelects changes in copy
a[2]=10
print(b)

b[2]=100
print(a)
c=[2,4,5]
d=[8,6,5]
print(c+d)
l1=[3,5,6]
print(l1*3)
#Tuples 
t1=(2,3,"rohit")
print(t1)