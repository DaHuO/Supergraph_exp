fr = open('/home/rafail/Desktop/input1.in', 'r')
fw = open ('/home/rafail/Desktop/output1.out', 'w')

t=fr.readline().rstrip()
count=1
for i in range(int(t)):
	n=fr.readline().rstrip()
	n=list(n)
	word=[]
	for j in n:
		if word==[]:
			word=j
		else:
			if (word[0]>j):
				word=word + j
			else:
				word= j + word
	s= ''.join(word)
	fw.write("Case #"+str(count)+": " + s +"\n")				
	count+=1	
