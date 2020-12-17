class add:
	def operate1(self):
		self.sum=self.a+self.b
		return self.sum;
class subtract:
	def operate2(self):
		self.diff=self.a-self.b
		return self.diff;
class multiply(add,subtract):
	def input(self):
		self.a=int(input("Enter the first no: "))
		self.b=int(input("Enter the second no: "))
	def operate3(self):
		self.mul=self.a*self.b
		return self.mul;
m=multiply()
m.input()
print(m.operate1())
print(m.operate2())
print(m.operate3())