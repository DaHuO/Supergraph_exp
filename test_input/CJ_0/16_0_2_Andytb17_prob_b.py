def tail(cakes, sign):
	'''
	@param cakes a list that represents a cake stack, with cakes[0] as the top cake
	@sign +1 or -1, with positive as the 'smile facing up'
	@return the largest index of the cake that has the desired sign
			-1 if there's no desired cake or cakes is empty
	'''
	for i in xrange(len(cakes)-1, -1, -1):
		if cakes[i] * sign > 0: return i 
	return -1

def steps(cakes, sign):
	'''
	@param see spe in tail()
	@return the optimal number of steps to make the cake stack to 'sign'
	'''
	total_n = len(cakes)
	cut = tail(cakes, -sign)
	if cut < 0: return 0
	return steps(cakes[:cut+1], -sign)+1

def converline(line):
	'''
	@param line a string input of the form '--++-+'
	@return an integer representation of line
	        '+' converted to '+1' and '-' to '-1'
	'''
	line_eles = list(line)
	return [ 2*(int(ele=='+')-.5) for ele in line_eles ]

def solve(file_in, file_out):
	'''
	solve the desired input and write to file_out
	'''
	fin = open(file_in)
	fout = open(file_out, 'w')
	num_cases = int(fin.readline())
	for i in xrange(num_cases):
		cakes = converline(fin.readline().strip())
		ans = str(steps(cakes, +1))
		fout.write('Case #'+str(i+1)+': '+ans+'\n')
	fin.close()
	fout.close()

solve('B-large.in.txt','output-b2.txt')