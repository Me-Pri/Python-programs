import array as a
a1=a.array('i',[5,4,3,2,1])
x=len(a1)
max=a1[0]
temp=0
i=0
for i in range (0,x):
	for j in range(i+1,x):
		if a1[i]>a1[j]:
			temp=a1[j]
			a1[j]=a1[i]
			a1[i]=temp
for i in range (0,x):
 print(a1[i])