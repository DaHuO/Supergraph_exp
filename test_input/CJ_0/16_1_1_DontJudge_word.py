import string
with open("/Users/danielvebman/Downloads/word.in.txt", "r") as input:
	cases = []
	for line in input:
		if line.rstrip().isdigit() == False:
			cases.append(line.rstrip())
	n = 0
	for case in cases:
		n+=1
		winner = case[0]
		print n
		case = case[1:]
		for c in case:
			if string.uppercase.index(c) > string.uppercase.index(winner[0]):
				winner = c + winner
			elif string.uppercase.index(c) < string.uppercase.index(winner[0]):
				winner = winner + c
			else:
				winner = c + winner

		with open("/Users/danielvebman/Downloads/word.out.txt", "a") as output:
			output.write("Case #"+str(n)+": "+winner+"\n")