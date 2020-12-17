class operate:
	squar=1
	cub=1
	def __init__(self,no):
		self.no=no
	def square(self):
		self.squar=self.no*self.no
		print("The square of {0} is {1} ".format(self.no,self.squar))
	def cube(self):
		self.cub=self.no*self.no*self.no
		print("The cube of {0} is {1} ".format(self.no,self.cub))
no=int(input("Enter a no: "))
op=operate(no);
op.square();
op.cube();
