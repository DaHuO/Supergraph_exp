import sys

def flip(l):
	re_l = []
	for ii in l:
		if ii == '-':
			re_l.append('+')
		elif ii == '+':
			re_l.append('-')
	return re_l

def get_no_man(s):
	s = [i for i in s]
	flips = 0
	while True:
		indices = [i for i, x in enumerate(s) if x == "-"]
		if len(indices) > 0:
			to_flip_index = max(indices) + 1
			s = flip(s[:to_flip_index]) + s[to_flip_index:]
			flips += 1
		else: 
			break

	return flips


fpath = sys.argv[1]

f = open(fpath, 'r')
with open(fpath, 'r') as f:
	content = f.read()

content = content.split('\n')

t = int(content[0]) #no. of test cases


for jj in range(1, t+1):
	print 'Case #{}: {}'.format(jj, get_no_man(content[jj]))