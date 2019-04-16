#問1:4つの属性を持つAppleクラスの定義
class Apple:
	def __init__(self,a,b,c,d):
		self.kind=a
		self.locality=b
		self.color=c
		self.sugar_content=d
		
apple=Apple("Jonagold","aomori","red","12")
print(apple)

#問2：円を表すCircleクラスの定義、面積を計算して返すareaメソッド
import math
class Circle:
	def __init__(self,d,r):
		self.diameter=d
		self.radius=r
	
	def length(self):
		return self.diameter*math.pi
	def area(self):
		return self.radius*self.radius*math.pi

circle=Circle(10,5)
print(circle.area())
print(circle.length())

#問3：三角形を表すTriangleクラスの定義、面積を返すareaメソッド、
class Triangle:
	def __init__(self,b,h):
		self.bottom=b
		self.height=h
	
	def area(self):
		return self.bottom*self.height/2

triangle=Triangle(4,8)
print(triangle.area())

#問4：六角形を表すHexagonクラスの定義、外周の長さを返すcalculate_perimeterメソッド
class Hexagon:
	def __init__(self,s1,s2,s3,s4,s5,s6):
		self.s1=s1
		self.s2=s2
		self.s3=s3
		self.s4=s4
		self.s5=s5
		self.s6=s6
		
	def calculate_perimeter(self):
		return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6

hexagon=Hexagon(1,2,3,4,5,6)
print(hexagon.calculate_perimeter())