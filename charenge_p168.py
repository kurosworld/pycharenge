##問1：RectangleクラスとSquareクラスの定義
##外周の長さを返すcalculate_perimeterメソッドの定義
##RectangleオブジェクトとSquareオブジェクトを作って、calculate_perimeterメソッドを呼ぶ
import math
#class Rectangle:
#	def __init__(self,w,l):
#		self.width=w
#		self.len=l
#		
#	def calculate_perimeter(self):
#		return self.width*2+self.len*2
#
#class Square:
#	def __init__(self,s1):
#		self.s1=s1
#		
#	def calculate_perimeter(self):
#		return self.s1*4
#		
#	#問2：Squareクラスにchange_sizeメソッドを定義
#	def change_size(self,new_size):
#		self.s1+=new_size
#		
#		
#rectangle=Rectangle(5,4)
#print("円周の長さ",rectangle.calculate_perimeter())
#square=Square(10)
#print("四角形の外周の長さ",square.calculate_perimeter())
#
#a_square=Square(100)
#print(a_square.s1)
#
#a_square.change_size(-10)
#print(a_square.s1)
#print("四角形の外周の長さ",a_square.calculate_perimeter())
#
#問3：Shapeクラスを定義、what_am_iメソッドを定義、
#RectangleクラスとSquareクラスにShapeクラスを継承させる
class Shape:
	def what_am_i(self):
		print("I am a shape.")

class Rectangle(Shape):
	def __init__(self,w,l):
		self.width=w
		self.len=l
		
	def calculate_perimeter(self):
		return self.width*2+self.len*2

class Square(Shape):
	def __init__(self,s1):
		self.s1=s1
		
	def calculate_perimeter(self):
		return self.s1*4
		
	#問2：Squareクラスにchange_sizeメソッドを定義
	def change_size(self,new_size):
		self.s1+=new_size
		

a_rectangle=Rectangle(20,50)
a_square=Square(9)
a_rectangle.what_am_i()
a_square.what_am_i()

#問4：HorseクラスとRiderクラスの定義、コンポジションを使用して馬に騎手を持たせる
class Horse:
	def __init__(self,name,owner):
		self.name=name
		self.owner=owner
		
class Rider:
	def __init__(self,nam):
		self.nam=nam
		
mike=Rider("Michael Jackson")
horse=Horse("栗毛",mike)
print(horse.name)
print(horse.owner)
print(horse.owner.nam)