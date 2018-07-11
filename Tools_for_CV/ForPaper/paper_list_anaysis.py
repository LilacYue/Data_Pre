
from collections import OrderedDict
def cvpr_list(txt):
	f = open(txt,"r")
	paper_name=[]
	authors_name={}
	k=0
	for line in f.readlines():
		line=line.lower()
		if k%4==0:
			#if k<10:
			words=line.split("\n")[0].split(" ")
			temp=[]
			for word in words:
				if ":" in word:
					#words[i]=word.split(':')[0]
					temp.append(word.split('-')[0])
				if "-" in word:
					#print(word)
					#words[i]=word.split('-')[0]
					temp.append(word.split('-')[1])
					temp.append(word.split('-')[0])
			for t in temp:
				words.append(t)
			#print("ok")
			paper_name.append(words)
			#print(words)
			#else:
			#print(authors_name)
				#exit()
		elif k%4==1:
			authors=line.split("\n")[0].split(",")
			for author in authors:
				if author not in authors_name:
					authors_name[author]=1
				else:
					authors_name[author]+=1
		k=k+1
		if k%1000==0:
			print(k)
				#paper_name
	auhtor_num=num_count(authors_name.values())
	auhtor_num=OrderedDict(sorted(auhtor_num.items(),key=lambda x: x[1]))
	authors_name=OrderedDict(sorted(authors_name.items(), key=lambda x: x[1]))
	save_res(authors_name,txt.split(".")[0]+"_author_num")
	#print("author_num:",txt.split(".")[0]+"_author_num")
	return paper_name,authors_name

def words_anlysis(paper_name,words):#,key):
	
	#```
	#words is cvpr_list
	#```
	num_count={}
	for word in words:
		word=word.lower()
		num_count[word]=0
	for name in paper_name:
		for i,word in enumerate(words):
			word=word.lower()
			if len(word.split(" "))==1:
				#print(word,len(word.split(" ")))
				#print(word,":::",paper_name)
				#exit()
				if word in name:
					num_count[word]+=1
					#if word==key:
						#print(name)
			else:
				temp=0
				for w in word.split(" "):
					if w not in name:
						break
					else:
						temp+=1
				if temp==len(word.split(" ")):
					num_count[word]+=1
	num_count=OrderedDict(sorted(num_count.items(), key=lambda x: x[1]))
	save_res(num_count,"num_count")
	return num_count

def save_res(di,name):
	f=open('./'+name+'.txt','w')
	for item in di:
		line=str(item)+" "+str(di[item])+"\n"
		f.writelines(line)
def num_count(set01):
	num_ = {}
	for item in set01:
		if item not in num_:
			num_[item]=1
		else:
			num_[item]+=1
	return num_
if __name__ == '__main__':
	txt ="./cvpr2018.txt"
	paper_name,authors_name=cvpr_list(txt)
	#find_words=raw_input("find_words: ")
	words=['detection','face','3D','object detection',"tracking","gan","weakly","re"]
	print(words_anlysis(paper_name,words))#,"re"))