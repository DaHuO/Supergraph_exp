def produce_next(s_in, char_in):
	if char_in >= s_in[0]:
		return char_in+s_in 
	else:
		return s_in + char_in

def last_word(s_in):
	temp_s = s_in[0]
	N = len(s_in)
	for i in range(1, N):
		temp_s = produce_next(temp_s, s_in[i])
	return temp_s


def solve(f, f_out):
	fin = open(f)
	fout = open(f_out, 'w')
	n = int( fin.readline().strip() )
	for i in xrange(n):
		s = fin.readline().strip()
		fout.write('Case #'+str(i+1)+': '+last_word(s)+'\n')
	fin.close()
	fout.close()


solve('A-large.in-2.txt','output_large.txt')