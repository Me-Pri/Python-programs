class Circle:
	def c_area(self):
		self.area1=radius*radius*3.14
		print(self.area1)
		return self.area1;
class Triangle:
	def t_area(self):
		self.area2=(base*height)/2
		print(self.area2)
		return self.area2;
class Area(Circle,Triangle):
	def __init__(self,radius):
		self.radius=radius
	def __init__(self,base,height):	
		self.base=base
		self.height=height
	def display(self):
		print("The area of the circle is: ",self.area1)
		print("The area of the triangle is: ",self.area2)
print("For circle..................................")
radius=int(input("Enter the radius of the circle: "))
a=Area(radius)
a.c_area()
print("For triangle...............................")
base=int(input("Enter the base of the triangle: "))
height=int(input("Enter the height of the triangle: "))
a=Area(base,height)
a.a_area()
#a.display()

