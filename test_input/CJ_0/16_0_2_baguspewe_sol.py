def flip(N, n):
	l = N[0:n]
	r = N[n:]
	l2 = [not a for a in l]
	l2.reverse()
	return l2+r

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t+1):
	N = [c is "+" for c in list(str(raw_input()))]

	knownM = [N]

	n = 0
	found = False
	if False in N:
		worklist = [[N,-1,0]]

		while(not found):
			[M,last_flip_n,n_flips] = worklist.pop(0)

			for j in xrange(1,len(M)+1):
				if j != last_flip_n:
					newM = flip(M, j)
					if False not in newM:
						found = True
						n = n_flips + 1
						break
					elif newM != M and newM not in knownM:
						worklist.append([newM, j, n_flips+1])
						knownM.append(newM)

	print "Case #{}: {}".format(i, n)
