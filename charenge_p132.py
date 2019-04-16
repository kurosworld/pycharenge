import csv

#csvファイル生成、書き込み
#with open("st.csv","w",newline='',encoding="cp932") as f:
#	w=csv.writer(f,delimiter=",")
#	w.writerow(["one","two","three"])
#	w.writerow(["four","five","six"])

#csvファイル読み込み出力
#with open("st.csv","r",encoding="cp932") as f:
#	r=csv.reader(f,delimiter=",")
#	for row in r:
#		print(row)
#		print(",".join(row))
#
#read_host=input("please [Enter]key")

#問2
print("なんの肉？")
value=input("解凍：")
with open("anser.txt","w",encoding="cp932") as f:
	f.write(value)

#問3
list=[["Top Gan","Risky Business","Minority Report"],["Titanic","The Revenant","Inception"],["Training Day","Man on Fire","Flight"]]
with open("st3.csv","w",newline='',encoding="cp932") as f:
	w=csv.writer(f,delimiter=",")
	w.writerow(list[0])
	w.writerow(list[1])
	w.writerow(list[2])
	