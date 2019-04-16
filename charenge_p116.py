list=["ウォーキング・デッド","アントラージュ","ザ・ソプラノ"]
for i in list:
	print(i)
	
for i in range(25,51):
	print(i)
	
for i, index in enumerate(list):
	print(i,index)

#数字あてプログラム
ans=[1,2,3,4,5]
while True:
	value=input("here:")
	if value == "q":
		break
	try:
		value=int(value)
		if value in ans:
			print("正解です")
		else:
			print("不正解です")
	except ValueError:
		print("数字を入力するか,qで修了します")
		
list1=[8,19,148,4]
list2=[9,1,33,83]
add=[]
for i in list1:
	for j in list2:
		add.append(i*j)
print(add)