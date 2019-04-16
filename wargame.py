#randomモジュールのshuffleメソッドを利用する
import random
from random import shuffle

class Card:
	#クラス変数[suits]と[values]（valuesの最初のNoneはリストのインデックス操作と値が一致するようにするため）
	suits=["spades","hearts","diamonds","clubs"]
	values=[None,None,
			"2","3","4","5","6","7","8","9",
			"10","Jack","Queen","King","Ace"]
	#suits=["spades","hearts","diamonds","clubs"]
	#values={"0":None,"1":None,"2":"2","3":"3","4":"4","5":"5",
	#		"6":"6","7":"7","8":"8","9":"9","10":"10",
	#		"11":"Jack","12":"Queen","13":"King","14":"Ace"}
		
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
		
#大小比較
#card1=Card(10,2)
#card2=Card(10,3)
#print(card1<card2)
#print(card1>card2)
#インスタンス変数valueとsuitを表示する、__repr__がないと出力は「<__main__.Card object at 0x000001E1DBC1AB70>」になる
#card=Card(3,2)
#print(card)

class Deck:
	def __init__(self):
		#シャッフル前のカードリスト
		self.init_cards=[]
		#52枚のカードリスト
		self.cards=[]
		#52枚のカードリスト(番号)
		self.list_num=[]
		#52枚のカードディクショナリー
		self.cards_dict={}
		for i in range(2,15):
			for j in range(4):
				self.init_cards.append(Card(i,j))
			
		#番号を入れる
		for i,card in enumerate(self.init_cards):
			self.list_num.append(i)
		
		#順番に並んだカードをシャッフルするshuffleメソッド(ここでは番号をシャッフルする)
		shuffle(self.list_num)
		for i,card in enumerate(self.list_num):
			#52枚のカードリストにシャッフルした番号で入れる
			self.cards.append(self.init_cards[self.list_num[i]])
		#辞書化前確認用
		#for i,card in enumerate(self.cards):
		#	print(self.list_num[i],card)
		
		print("\n")
		#2つのリストを辞書にする
		self.cards_dict=dict(zip(self.list_num,self.cards))
		#辞書化後確認用
		#for i in self.cards_dict:
		#	print(i,self.cards_dict[i])
		
	#メソッド名を適切なものに変更
	def draw(self):
		#print(self.cards)
		#print(len(self.cards))
		if len(self.cards)==0:
			return
		#おそらくself.cards.pop()だと一回目であるプレイヤー1は52番を返し2回目であるプレイヤー2は51番を返している
		#その次はp1が50、p2が49とかいう具合になっていて、結局p1が全部勝ってしまうんやね
		#return self.cards.pop() #元のやつ
		#↓のようにすればただしく動くはず
		self.take_num=random.choice(self.list_num)
		self.result=self.cards[self.take_num]
		#選んだ後に削除しているので↑はrandom.sampleじゃなくて、random.choiceを使用するのがミソ
		#↓の意味は[self.list_numからランダムに選ばれたインデックスの値（self.take_num）] [self.take_numに対応したself.list_numの値(pop()で消す値)] [self.take_numに対応したself.cardsの値(pop()で消す値)]
		#print(self.take_num,self.list_num.pop(self.take_num),self.cards.pop(self.take_num))
		self.list_num.pop(self.take_num)
		self.cards.pop(self.take_num)
		#pop()されたかの確認用
		#for i,card in enumerate(self.cards):
		#	print(card)
		return self.take_num
		
#deck=Deck()
#print(deck.cards)
#for i,card in enumerate(deck.cards):
#	print(i,card)

class Player:
	def __init__(self,name):
		self.name=name
		self.wins=0
		self.card=None
		
class Game:
	def __init__(self):
		name1=input("プレーヤー1の名前	")
		name2=input("プレーヤー2の名前	")
		#Deckのオブジェクトを作ってインスタンス変数deckに格納する
		self.deck=Deck()
		#print(self.deck.cards)
		#入力された変数を使ってPlayerオブジェクトを作る
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
		#print(cards[1])
		print("戦争を始めます")
		while len(cards) >= 2:
			m="\nqで終了、それ以外のキーでPlay:"
			response=input(m)
			if response == 'q':
				break
			#print(self.p1.card,self.p2.card)
			self.p1.card=self.deck.draw()
			self.p2.card=self.deck.draw()
			#print(self.p1.card,self.p2.card)
			#print(self.p1.name,self.p2.name)
			#プレイヤー1はKing of hearts、プレイヤー2はJack of spadesを引きました　という表示をするだけ
			self.print_draw(self.p1,self.p2)
			#if self.p1.card>self.p2.card:
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