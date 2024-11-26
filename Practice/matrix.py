matrix=[]
for i in range(3):
  row=[]
  for j in range(3):
    print(f"Enter row {i+1} and colomn {j+1} value :")
    value=int(input())
    row.append(value)
  matrix.append(row)

z=0
nz=0
for i in range(3):
  for j in range(3):
    if(matrix[i][j]!=0):
      nz=nz+1
    else:
      z=z+1
rep=[]
for i in range(3):
  for j in range(3):
    if(matrix[i][j]!=0):
      rep.append(i,j,matrix[i][j])
print(rep)


print("No of zero Values:",z)
print("No of Non-zero Values:",nz)

if(nz>z):
  print("This is not a Sparse matrix")
else:
  print("This is a sparse matrix")
print(matrix)