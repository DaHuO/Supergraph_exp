prob2 = open('input.in', 'r')


T = int(prob2.readline())
answers=[]

for i in xrange(T):
	n = prob2.readline().strip()
	if '-' not in n:
		answers.append('0')
	else:
		count=0
		#print len(n)
		for j in xrange(1,len(n)):
			#print i,j
			#print n[j]
			if n[j]!=n[j-1]:
				count+=1
		if n[-1]=='-':
			count+=1
		answers.append(str(count))

prob2.close()

sol2 = open('sol2.txt','w')
for i in range(len(answers)):
	sol2.write('Case #'+str(i+1)+': '+answers[i]+'\n')