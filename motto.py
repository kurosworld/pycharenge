"""
すべてのオブジェクトはクラスのインスタンスである
クラスから作られるオブジェクトをインスタンスと呼ぶ
本書の文脈ではオブジェクトと言ったときはインスタンスのことを指す
"""

#class Lion:
#	def __init__(self,name):
#		self.name=name
#		
#	def __repr__(self):
#		return self.name
#		
#lion=Lion("Dilbert")
#print(lion)

class AlwaysPositive:
	def __init__(self,number):
		self.n=number
		
	def __add__(self,other):
		return abs(self.n+other.n)
		
x=AlwaysPositive(-20)
y=AlwaysPositive(10)

print(x+y)

class Person:
	def __init__(self):
		self.name="Bob"
	
#[is] オブジェクトが同一かどうか比較するTrue/False	
bob=Person()
same_bob=bob
print(bob is same_bob)

another_bob=Person()
print(bob is another_bob)

#ある変数がNoneかどうかを調べるときにも使用する「is」
s=10
if s is None:
	print("s はNone:(")
else:
	print("s はNoneじゃない")
	
s=None
if s is None:
	print("s はNone")
else:
	print("s はNoneじゃない:(")