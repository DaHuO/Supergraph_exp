fr = open('/home/rafail/Desktop/code_jam/input2.in', 'r')
fw = open ('/home/rafail/Desktop/code_jam/output2.out', 'w')

t=fr.readline().rstrip()

for j in range(int(t)):
	s=fr.readline().rstrip()
	length=len(s)
	i=length-1
	swaps=0
	slist=list(s)
	while("-" in slist):
		while(1):
			if (s[i]=="+" and i>=0):
				i-=1
			else:
				break
		if (s[0]=="+"):
			counter=0
			while(s[counter+1]=="+" and counter < length ):
				counter+=1
			slist=list(s)
			slist1=slist[:counter+1]
			slist2=slist[counter+1:]		
			for k in range(counter+1):
				if (slist1[k]=="+"):
					slist1[k]="-"			
			slist= slist1 + slist2	
			slist=slist[:i+1]
			for k in range(i+1):
				if (slist[k]=="+"):
					slist[k]="-"
				else:
					slist[k]="+"
			slist.reverse()	
			s= ''.join(slist)
			swaps = swaps+2
		else:
			slist=list(s)
			slist=slist[:i+1]
			for k in range(i+1):
				if (slist[k]=="+"):
					slist[k]="-"
				else:
					slist[k]="+"
			slist.reverse()	
			s= ''.join(slist)
			swaps = swaps+1	
	fw.write("Case #"+str(j+1)+": " + str(swaps) + "\n")
fw.close()
fr.close()
			
