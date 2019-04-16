#randomモジュールのshuffleメソッドを利用する
import random
from random import shuffle

class Card:
	suits=["spades","hearts","diamonds","clubs"]
	values=[None,None,
			"2","3","4","5","6","7","8","9",
			"10","Jack","Queen","King","Ace"]
		
	def __init__(self,v,s):
		"""スートも値も整数値です"""
		self.value=v
		self.suit=s
		
	def __lt__(self,c2):
		if self.value<c2.value:
			return True,"lt-1"
		if self.value==c2.value:
			#冗長を排除
			return self.suit<c2.suit
		return False,"lt-2"
		
	def __gt__(self,c2):
		if self.value>c2.value:
			return True,"gt-1"
		if self.value==c2.value:
			#冗長を排除
			return self.suit>c2.suit
		return False,"gt-2"
		
	def __repr__(self):
		v=self.values[self.value]+" of "+self.suits[self.suit]
		return v
		
class Deck:
	def __init__(self):
		#シャッフル前のカードリスト
		self.init_cards=[]
		#52枚のカードリスト
		self.cards=[]
		#シャッフル前のカードリスト(番号)
		self.init_list=[]
		#52枚のカードリスト(番号)
		self.list_num=[]
		for i in range(2,15):
			for j in range(4):
				self.init_cards.append(Card(i,j))
			
		#カードの枚数分の番号を追加
		for i,card in enumerate(self.init_cards):
			self.init_list.append(i)
			self.list_num.append(i)
		
		shuffle(self.list_num)
		for i,card in enumerate(self.init_list):
			#52枚のカードリストにシャッフルした番号で追加
			self.cards.append(self.init_cards[self.list_num[i]])
			
		#2つのリストを辞書にする
		#self.cards_dict=dict(zip(self.list_num,self.cards))
	
	#メソッド名を適切なものに変更
	def draw(self):
		print(len(self.cards),len(self.list_num),len(self.init_list))
		if len(self.cards)==0:
			return
		self.take_num=random.choice(self.init_list)
		print(self.take_num)
		self.result=self.cards[self.take_num]
		#self.list_num.pop(self.take_num)
		#self.cards.pop(self.take_num)
		return self.take_num,self.result

class Player:
	def __init__(self,name):
		self.name=name
		self.wins=0
		self.card=None
		
class Game:
	def __init__(self):
		name1=input("プレーヤー1の名前	")
		name2=input("プレーヤー2の名前	")
		self.deck=Deck()
		self.p1=Player(name1)
		self.p2=Player(name2)
		
	#メソッド名を適切なものに変更
	def print_winner(self,winner):
		w="このラウンドは{}が勝ちました"
		#冗長を排除
		print(w.format(winner.name))
		
	#メソッド名を適切なものに変更	
	def print_draw(self,p1,p2):
		d="{}は{}、{}は{}を引きました"
		#冗長を排除
		print(d.format(p1.name,p1.card,p2.name,p2.card))
		
	def play_game(self):
		cards=self.deck.cards
		print("戦争を始めます")
		while len(cards) >= 2:
			m="\nqで終了、それ以外のキーでPlay:"
			response=input(m)
			if response == 'q':
				break
			self.p1.card=self.deck.draw()
			self.p2.card=self.deck.draw()
			self.print_draw(self.p1,self.p2)
			if self.p1.card>self.p2.card:
				self.p1.wins+=1
				self.print_winner(self.p1)
			else:
				self.p2.wins+=1
				self.print_winner(self.p2)
				
			
		win=self.winner(self.p1,self.p2)
		print("ゲーム終了、{}の勝利です".format(win))
		breakdown=[self.p1.wins,
					self.p2.wins]
		print(breakdown)
		
	def winner(self,p1,p2):
		if p1.wins>p2.wins:
			return p1.name
		if p1.wins<p2.wins:
			return p2.name
		return "引き分け"
		
	
game=Game()
game.play_game()
