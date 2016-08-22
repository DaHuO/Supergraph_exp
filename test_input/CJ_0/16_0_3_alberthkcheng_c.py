import numpy as np
import math

n = int(raw_input())

def find_factor(n):
	f = 1
	for i in range(2, int(math.sqrt(n))+1):
		if n % i == 0:
			f = i
			break
	return f

def find_factor_str(s):
	return map(lambda x: find_factor(int(s,x)), range(2,11))



for i in range(n):
	[N, J] = map(int, raw_input().split(" "))
	print "Case #" + str(i+1) + ": " 

	min_s = '1' + '0' * (N - 2) + '1'
	# print min_s 
	n = int(min_s,2)
	# print n
	while J > 0:
		s = np.binary_repr(n)
		result = find_factor_str(s)
		if not 1 in result:
			print str(s) + ' ' + ' '.join(map(str,result))
			# print map(lambda x: int(s,x), range(3,11))
			J -= 1
		n += 2