fin = open('A-large.in')
fout = open('A-large.out', 'w+')
cases = int(fin.readline())
i = 0
for case in range(0, cases):
	word = fin.readline()

	i += 1
	firstCh = word[0:1]
	word = word[1:]
	lastword = firstCh
	for ch in word: 
		if(ch >= firstCh):
			lastword = ch + lastword
			firstCh = ch
		else:
			lastword = lastword + ch
	
	fout.write('Case #' + str(i) + ': ' + lastword)
fin.close()
fout.close()