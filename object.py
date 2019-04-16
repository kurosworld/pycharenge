##Orangeクラス
#class Orange:
#	#特殊メソッド
#	def __init__(self,w,c):
#		#2つのインスタンス変数
#		self.weight=w
#		self.color=c
#		self.mold=0 #温度を表すインスタンス変数追加
#		print("Created!")
#	
#	#オレンジにほかの特性を表すメソッド
#	def rot(self,days,temp):
#		"""temp(温度)は摂氏"""
#		self.mold=days*temp


##新しいオブジェクトを作ることをクラスのインスタンス化という
#org=Orange(10,"orange")
##オブジェクトを生成した後にインスタンス変数の値を取得
#print(org.weight)
#print(org.color)
##インスタンス変数の値の変更
#org.weight=100
#org.color="light orange"
#print(org.weight)
#print(org.color)

##Orangeクラスを利用して複数のオレンジオブジェクトを作る
#org1=Orange(4,"light orange")
#org2=Orange(8,"dark orange")
#org3=Orange(14,"yellow")

#orange=Orange(200,"orange")
#print(orange.mold)
#orange.rot(10,37)
#print(orange.mold)

#長方形を表すクラス
class Rectangle:
	def __init__(self,w,l):
		#2つのインスタンス変数
		self.width=w
		self.len=l
	
	#面積を計算するメソッド	
	def area(self):
		return self.width*self.len
	
	#新たに引数をインスタンス変数に代入するメソッド
	def change_size(self,w,l):
		self.width=w
		self.len=l

rectangle=Rectangle(10,20)
print(rectangle.area())
rectangle.change_size(20,40)
print(rectangle.area())