no=int(input("Enter the no of elements: "))
a=[]
print("Enter the elements of 1st matrix........")
for i in range(no):
	a1=[]
	for j in range(no):
		a1.append(int(input("Enter the element {0}{1}: ".format(i,j))))
	a.append(a1)
b=[]
print("Enter the elements of 2nd matrix......")
for i in range(no):
	b1=[]
	for j in range(no):
		b1.append(int(input("Enter the element {0}{1}: ".format(i,j))))
	b.append(b1)
result=[[0,0,0],[0,0,0],[0,0,0]]
multiply=[[0,0,0],[0,0,0],[0,0,0]]
print("The product of two matrix is.........")
for i in range(no):
	for j in range(no):
		for k in range(no):
			multiply[i][j]=a[i][k]*b[k][j]
			result[i][j]+=multiply[i][j]
for i in range(no):
	for j in range(no):
		print(result[i][j],end="")
	print("\r")
