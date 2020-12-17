class factorial:
	no=0;
	fact=1;
	def input(self):
		self.no=int(input("Enter the no of terms: "))
	def factor(self):
		for i in range(1,self.no+1):
			self.fact=self.fact*i
		print("The factorial of {0} is {1}".format(self.no,self.fact))
fac=factorial();
fac.input();
fac.factor();