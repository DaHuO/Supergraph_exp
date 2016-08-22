

for n in range(int(input())) :
	word=input()
	res=""
	for c in word :
		if len(res)==0 :
			res+=c
		else : 
			if ord(c)>=ord(res[0]) :
				res=c+res
			else :
				res=res+c
	print("Case #"+str(n+1)+": "+res)