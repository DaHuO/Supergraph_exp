def main():
	t = int(raw_input())
	for i in xrange(1, t+1):
		S = raw_input()
		print "Case #{}: {}".format(i, process(S))

def process(S):
	moves = 0
	i = getLowestBlank(S)
	
	while i != 'ALL_HAPPY':
		j = 0
		for e in S:
			if e == '-':
				break
			j += 1

		if j != 0:
			moves += 1
			S = flip(S, j)
		
		moves += 1
		S = flip(S, i)
		
		i = getLowestBlank(S)
	
	return moves

def getLowestBlank(S):
	i = 0
	for e in reversed(S):
		if e == '-':
			return len(S) - i
		i += 1
	
	return 'ALL_HAPPY'
	
def flip(S, i):
	S1, S2 = S[:i], S[i:]
	new_S1 = ""
	
	for s in reversed(S1):
		if s == '+':
			new_S1 += '-'
		else:
			new_S1 += '+'
	
	return new_S1 + S2

main()
