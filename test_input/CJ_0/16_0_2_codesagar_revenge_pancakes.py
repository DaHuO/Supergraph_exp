inpt = open('input','r')
oupt = open('output','w')

n = inpt.readline().rstrip('\n')
#n = raw_input('')
for z in range(int(n)):
	x = inpt.readline().rstrip('\n')
#	x = raw_input('')
	l = list(x)
	cnt = 0
	length = len(l)
	for i in range(1,length):
		if l[int(i)-1]!=l[int(i)]:
			cnt = cnt + 1
	if l[-1] == '-':
		ou = 'Case #'+str(z+1)+': '+str(cnt+1)+'\n'
		oupt.write(ou)
	else:
		ou = 'Case #'+str(z+1)+': '+str(cnt)+'\n'
		oupt.write(ou)



