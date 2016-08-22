#code jam_1a

from itertools import permutations

n = int(raw_input())

for i in range(n):
	palavra = raw_input()
	nPalavra = palavra[0]
	
	for p in range(1, len(palavra)):
		if palavra[p] >= nPalavra[0]:
			nPalavra = palavra[p] + nPalavra
		else:
			nPalavra += palavra[p]
	print "Case #%d: %s" %(i + 1, nPalavra)
