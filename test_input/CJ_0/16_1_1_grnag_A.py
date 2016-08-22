# 2016 round 1A - Problem A

inFile =  open("A.large.in", "r")

T = int(inFile.readline().split()[0])

case = 1

while case <= T:
	N = inFile.readline().split()[0]
		
	ll = len(N)
	count = 1
	ss = ""
	ss += N[0]
	while count < ll:
		if ss[0] > N[count]:
			ss += N[count]
		else:
			ss = N[count] + ss
		
		count += 1
#		print ss
		
		
	
	print "Case #{}: {}".format(case, ss)
	case += 1
