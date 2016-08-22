f = open('input.txt')
line = f.readline().split()
num_test_cases = int(line[0])
results = []

for i in xrange(num_test_cases):
	line = f.readline().split()
	S = line[0]
	words = set()

	words.add(S[0])
	white_board = str(S[0])
	for j in xrange(1, len(S)):
		l = S[j]
		if(l >= white_board[0]):
			white_board = l + white_board
		else:
			white_board = white_board + l
	results.append("Case #" + str(i + 1) + ": " + white_board + '\n')


f2 = open('output.txt','w')
for i in xrange(num_test_cases):
	f2.write(results[i])
f.close()
f2.close()