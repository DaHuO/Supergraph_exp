import sys
T=int(sys.stdin.readline())
#T=1
for a in range(1,T+1):
	string = sys.stdin.readline()
	#string = "CODE"
	lst = []
	lst.append(string[0])
	for c in range(1,len(string)):
		if string[c] < lst[0]:
			lst.append(string[c])
			#print lst
		else:
			lst.insert(0,string[c])
			#print lst
	main = "".join(lst)
	print "Case #"+str(a)+": "+main,


