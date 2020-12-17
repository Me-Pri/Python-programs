def fun(arg1,arg2):
	if arg1>arg2:
		test=arg1
	else:
		test=arg2
	return test;
arg1=int(input("Enter the first no: "))
arg2=int(input("Enter the second no: "))
larger=fun(arg1,arg2);
print(larger,"is the larger no")