x=int(input("Enter a no: "))
i=0
if x==1:
	flag=2
elif x==2:
	flag=1
else:
	for i in range (2,x):
		if x%i==0:
			flag=0
			break
		else:
			flag=1
if flag==2:
	print("1 is neither prime nor composite")
elif flag==1:
	print(x,"is a prime no")
else:
	print( x,"is not a prime no")		