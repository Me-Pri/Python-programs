import numpy
no=int(input("Enter the no of terms: "))
a=[]
for i in range(no):
	a1=[]
	for j in range(no):
		a1.append(int(input("Enter the {0}{1} element: ".format(i,j))))
	a.append(a1)
print("the elements of first matrice is........")
for i in range(no):
	for j in range(no):
		print(a[i][j],end="")
	print("\r")
b=[]
for i in range(no):
	b1=[]
	for j in range(no):
		b1.append(int(input("Enter the element {0}{1}: ".format(i,j))))
	b.append(b1)
print("The elements of second matrice is........")
for i in range(no):
	for j in range(no):
		print(b[i][j],end="")
	print("\r")
for i in range(no):
	for j in range(no):
		result[i][j]=a[i][j]+b[i][j]
print("The sum of two matrices is..........")
for i in range (no):
	for j in range(no):
		print(numpy.add(a,b),end="")
	print("\r")
