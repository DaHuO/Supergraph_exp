t = int(raw_input())
for case in range(1,t+1):
	s = raw_input()
	n = len(s)
	if n == 0: 
		print "Case #"+str(case)+": "
		continue
	lst = [s[0]]
	for i in range(1,n):
		if ord(s[i]) >= ord(lst[0]):
			lst.insert(0,s[i])
		else:
			lst.append(s[i])
	print "Case #"+str(case)+":", "".join(lst)

