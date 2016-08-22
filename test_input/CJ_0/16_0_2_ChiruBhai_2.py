bin={}
pl=0
def yo(inp,m):
	fir = ""
	fstr = ""
	for i in range(len(inp)-1,-1,-1):
		if inp[i] != '-':
			continue
		else:
			for num in inp[0:i+1]:
				if num == '-':
					fir+='+'
				else:
					fir+='-'
			leng = len(inp)-len(inp[0:i+1])
			fstr = fir+inp[i+1:i+1+leng]
			#print(fstr,m)
			m+=1
			#print(m)
			bin[pl]=(m)
			#print(bin)
			yo(fstr,m)
			break
no = eval(input())
l = 1
while no>0:
	inp = str(input())
	bin[pl]=0
	yo(inp,0)
	print("Case #"+str(l)+': '+str(bin[pl]))
	no-=1
	l+=1
	pl+=1