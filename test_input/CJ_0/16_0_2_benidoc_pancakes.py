#! python
def flips(pancakes):
	flippies = 0
	noHappies = 1
	onaSadRun = 0
	for p in pancakes: 
		if noHappies:
			if p == '+':
				noHappies = 0
			else:
				flippies = 1
		else:
			if not onaSadRun and p == '-':
				onaSadRun = 1
				flippies += 2
			elif onaSadRun and p == '+':
				onaSadRun = 0
	return flippies

fin = open('B-large.in')
fout = open('large_output.txt', 'w+')
cases = int(fin.readline())
i = 1
for c in range(0, cases):
	pancakes = fin.readline()
	fout.write('Case #' + str(i) + ': ' + str(flips(pancakes)) + '\n')
	i += 1
fin.close()
fout.close()