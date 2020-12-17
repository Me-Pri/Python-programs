no=int(input("Enter a no: "))
rev=0
while no>0:
	remin=no%10
	rev=(rev*10)+remin
	no=no//10
print(rev)
