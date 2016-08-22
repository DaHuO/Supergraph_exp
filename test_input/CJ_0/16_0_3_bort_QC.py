import sys
from math import sqrt

def solve(s):
	N, J = map(int, s.split(' '))
	maxmid = 2 ** (N-2)

	jams = {}
	for i in range(maxmid):
		s = "1" + "{0:b}".format(i).zfill(N - 2) + "1"
		factors = []

		for b in range(2, 11):
			f = factor(int(s, b))
			if f:
				factors.append(f)
			else:
				break

		if len(factors) == 9:
			jams[s] = factors
			if len(jams) == J:
				return jams


def factor(n):
	for i in range(2, int(sqrt(n) + 1)):
		if n % i == 0: 
			return i

	return None


with open('C-small-attempt0.in') as f, open('C-small.out', 'w') as o:
	lines = f.readlines()

	case = 1
	for line in lines[1:]:
		sol = solve(line.strip())
		text = '\n'.join(['{0} {1}'.format(jc, ' '.join(map(str, sol[jc]))) for jc in sol.keys()])

		o.write("Case #{0}:\n{1}\n".format(case, text))
		#print("Case #{0}: {1}\n".format(case, solve(line.strip())))
		case += 1
	