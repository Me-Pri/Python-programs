a=int(input("Enter the first no: "))
b=int(input("Enter the second no: "))
class Add:
	def operate1(self):
		self.sum=self.a + self.b
		print("The sum of {0} and {1} is {2} ".format(self.a,self.b,self.sum))
class Subtract(Add):
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def operate2(self):
		self.diff=self.b-self.a
		print("The difference of {0} and {1} is {2} ".format(self.a,self.b,self.diff))
s=Subtract(a,b)
s.operate1()
s.operate2()