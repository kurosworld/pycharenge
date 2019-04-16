#カプセル化
#class Data:
#	def __init__(self):
#		self.nums=[1,2,3,4,5]
#		
#	def change_data(self,index,n):
#		self.nums[index]=n
#
#data_one=Data()
#data_one.nums[0]=100
#print(data_one,"\n",data_one.nums)
#
#data_two=Data()
#data_two.change_data(0,100)
#print(data_two,"\n",data_two.nums)
#
#class PublicPrivateExample:
#	def __init__(self):
#		self.public="safe"
#		self._unsafe="unsafe"
#		
#	def public_method(self):
#		#clientが使ってもよい
#		pass #パス文は、文が必須な構文でも何もしない場合に使う
#		
#	def _unsafe_method(self):
#		#clientは使うべきではない
#		pass #パス文は、文が必須な構文でも何もしない場合に使う
#
#publicprivateexample=PublicPrivateExample()
#public=publicprivateexample.public
#private=publicprivateexample._unsafe
#print(public,private)

#抽象化...本質的な特徴だけを集めた状態にする手順のこと
#class Person:
#	def __init__(self):
#		self.men="男"
#		self.women="女"
#
#ポリフォーリズム
#print関数のように「同じインターフェースでありながら、データ型に合わせて異なる動作をする機能」を提供すること
#if isinstance(オブジェクトが,指定のインスタンスの型であれば)：→true

#継承
#class Shape:
#	def __init__(self,w,l):
#		self.width=w
#		self.len=l
#		
#	def print_size(self):
#		print("{} by {}".format(self.width,self.len))
#		
#class Square(Shape):
#	def area(self):
#		return self.width*self.len
#		
#	#メソッドオーバーライド
#	def print_size(self):
#		print("I am {} by {}".format(self.width,self.len))
#
#a_square=Square(20,20)
#print(a_square.area())
#a_square.print_size()

#コンポジション[has-a関係]、別クラスのオブジェクトを変数として持たせるという構造概念
#犬（飼い犬）クラス
class Dog:
	def __init__(self,name,breed,owner):
		self.name=name
		self.breed=breed
		self.owner=owner

#人(飼い主)クラス
class Person:
	def __init__(self,name):
		self.name=name

#Dogオブジェクト作成時にその犬の飼い主としてPersoonオブジェクトを渡す
mick=Person("Mick Jappar")
stan=Dog("Stanley","Bulldog",mick)
print(stan.owner.name)