for _ in range(input()):
	a = raw_input()
	m = ""
	for i in a[::-1]:
		if(m == "" and i == "+" ):
			continue
		elif(m == "" and i == "-"):
			m += i
		elif( m[-1] == i):
			continue
		else:
			m += i
	print "Case #"+str(_ + 1)+": "+str(len(m))
