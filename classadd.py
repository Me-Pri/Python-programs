class sum:
	a=0;
	b=0;
	sum1=0
	def input(self):
		self.a=int(input("Enter the first no: "))
		self.b=int(input("Enter the second no: "))
	def add(self):
		self.sum1=self.a+self.b
		print("the sum of {0} and {1} is {2}".format(self.a,self.b,self.sum1))
s=sum();
s.input();
s.add();