import random
print ("ファイルの操作編\r\n")
dict_file_cmd={0:"file ディレクトリ名 -name ファイル名",
				1:"grep 文字列パターン 検索対象ファイル",
				2:"head ファイル名",
				3:"locate ファイル名",
				4:"tail ファイル名"}
				
dict_file_desc={0:"指定した名前のファイルを指定したディレクトリ以下から検索する",
				1:"指定した文字列が含まれる行をファイルから抜き出して表示する",
				2:"指定したファイルの先頭10行を表示する",
				3:"指定した名前のファイルを検索する",
				4:"指定したファイルの末尾10行を表示する"}


#以降は編集しなくてよいぞ
q=0
time=0
len_dict_file_cmd=len(dict_file_cmd)
list_template = list(range(len_dict_file_cmd))
list_template_random=random.sample(list_template, len_dict_file_cmd)
for i in range(0,(len_dict_file_cmd)):
	q=i+1
	r=list_template_random[i]
	print ("問"+str(q)+"\t"+(dict_file_cmd[r]))
	input_anser = input("説明:\t")
	anser=(str(input_anser)==(dict_file_desc[r]))
	if anser:
		print("...正解\r\n")
		time=time+1
	elif not anser:
		print("正：\t"+(dict_file_desc[r])+"\r\n")

print("正解数\t"+str(time)+"/"+str(q)+"\r\n")