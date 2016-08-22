
with open('B-large.in') as f:
	lines = f.read().splitlines()
	T = int(lines[0])
	N = lines[1:]
	f.close()

def getMinFlip(S):
	blocks = S.split('+')
	N_Blank = len(filter(lambda a : '-' in a, blocks))
	if '-' in blocks[0]:
		return 2*(N_Blank -1) +1
	else: 
		return 2*N_Blank
	
with open('output.txt','wb') as output:
	for i in range(T):
		print >> output, 'case #{0}: {1}'.format(i+1,getMinFlip((N[i])))
	output.close()

