def find_divider(num):
	upper = int(num**0.5)
	for div in xrange(2,upper+1):
		if num%div == 0: return div
	return -1

def B2N(binaryString, base):
	if binaryString[1] == 'b': binaryString = binaryString[2:]
	l = list(binaryString)
	length = len(l)
	out_num = 0
	for i in xrange(length):
		if l[i] == '1':
			pwr = length-i-1
			out_num += base**(pwr)
	return out_num

def jam_coin(binary):
	dividers = list()
	for base in xrange(2, 10+1):
		div = find_divider(B2N(binary, base))
		if div > 0:
			dividers.append(div)
		else:
			break
	if len(dividers) == 9:
		return True, dividers
	return False, []

def solve(file_in, file_out):
	fin  = open(file_in)
	fout = open(file_out, 'w')
	num_cases = int(fin.readline())

	for i in xrange(num_cases):
		fout.write('Case #'+str(i+1)+':\n')
		N,J = [ int(ele) for ele in fin.readline().strip().split(' ') ]
		counter = 0
		starting = 2**(N-1)+1
		for ii in xrange(2**(N-2)-1):
			binary = bin(starting+2*ii)[2:]
			valid, dividers = jam_coin(binary)
			if valid:
				fout.write(binary+' ')
				for div in dividers:
					fout.write(str(div)+' ')
				fout.write('\n')
				counter += 1
				if counter == J: break
	fin.close()
	fout.close()

solve('C-small-attempt0.in.txt','output1.txt')




