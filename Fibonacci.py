x=int(input("Enter the no of terms: "))
firstterm=0
sum=0
secondterm=1
no2=0
print("The Fibonacci series of {0} terms is........".format(x))
while(no2<x):
	if sum<=0:
		sum=no2
		print(sum)
	else:
		sum=firstterm+secondterm
		print(sum)
		firstterm=secondterm
		secondterm=sum
	no2=no2+1

		
		
		
			