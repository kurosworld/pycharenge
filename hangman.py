import random

def hangman(word):
	wrong=0
	stages=["",
			"______      ",
			"|           ",
			"|     |     ",
			"|     0     ",
			"|   ＼|／   ",
			"|     |     ",
			"|   ／ ＼   ",
			"|           "
			]
	rletters=list(word)
	board=["_"]*len(word)
	win=False
	print("Hello Hangman")
	
	while wrong<len(stages)-1:
		print("\n")
		msg="1文字を予想してね"
		char=input(msg)
		if char in rletters:
			cind=rletters.index(char)
			board[cind]=char
			rletters[cind]='$'
		else:
			wrong+=1
		print(" ".join(board))
		e=wrong+1
		print("\n".join(stages[0:e]))
		if "_" not in board:
			print("you win")
			print(" ".join(board))
			win=True
			break
	
	if not win:
		print("\n".join(stages[0:wrong+1]))
		print("you loss. 正解は{}".format(word))

word_list=["animal","vertebrata","mammals","omnivore","cat"]
r=random.choice(word_list)
hangman(r)