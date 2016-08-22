def flip(seq, to):

	flipped_seq = ''

	for char in range(0,to):
		if(seq[char] == '-'):
			flipped_seq = flipped_seq + '+'
		else:
			flipped_seq = flipped_seq + '-'

	return flipped_seq + seq[to:len(seq)]


def findLastMinus(seq):
	position = -1
	for i in range(len(seq)-1,-1,-1):
		if(seq[i]=='-'):
			position = i
			return position
	return position


f = open('input.txt')
f_out = open('output.txt', 'w')
inp = f.read().split('\n')
f.close()

jock = 'schmooockel'

cases = inp[0]

for case in range(1,int(cases)+1):
	f_out.write('Case #' + str(case) + ': ')
	seq = inp[case]
	minus = findLastMinus(seq)
	count = 0
	while(minus > -1):
		seq = flip(seq,minus+1)
		count = count + 1
		minus = findLastMinus(seq)
	f_out.write(str(count))
	f_out.write('\n')


