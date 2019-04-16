#問1：Squareクラスにsquare_listクラス変数を追加、
class Shape():
	def what_am_i(self):
		print("I am a shape.")
	
class Square(Shape):
	square_object_list=[]
	square_argument_list=[]
	
	def __init__(self,s1):
		self.s1=s1
		#※1、そのオブジェクトをリストに追加している
		self.square_object_list.append(self)
		#こっちはリストに引数を追加している
		self.square_argument_list.append(self.s1)
		
	def calculate_perimeter(self):
		return self.s1*4
		
	def what_am_i(self):
		super().what_am_i()
		print("I am Square.")
		
	#問２
	def __repr__(self):
		return "{}by{}by{}by{}".format(self.s1,self.s1,self.s1,self.s1)
		
#Squareクラスのオブジェクトが作られるたびに、※1
a_square=Square(29)
print(Square.square_object_list)
print(Square.square_argument_list)
another_square=Square(93)
print(Square.square_object_list)
print(Square.square_argument_list)

#問2：Squareクラスのオブジェクトをprint関数に渡したら、
#４辺それぞれの長さを出力しよう
b_square=Square(29)
print(b_square)

#問３：２つのパラメータを受け取る関数を書こう。
def compare(obj1,obj2):
	return obj1 is obj2
	
print(compare("a","b"))