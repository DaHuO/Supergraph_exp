import sys

cache = { '': 0, '-': 1, '+': 0 }

def solve(s):
	if s in cache:
		return cache[s]

	if '-' not in s:
		ans = 0
	elif s[-1] == '+':
	 	ans = solve(s[:-1])
	elif s[0] == '-': 
		ans = 1 + solve(flip(s))
	else:
		i = s.index('-')
		ans = 1 + solve(flip(s[:i]) + s[i:])

	cache[s] = ans
	return ans


def flip(s):
	return ''.join('+' if s[-(c + 1)] == '-' else '-' for c in range(len(s)))

with open('B-large.in') as f, open('B-large.out', 'w') as o:
	lines = f.readlines()

	case = 1
	for line in lines[1:]:
		o.write("Case #{0}: {1}\n".format(case, solve(line.strip())))
		#print("Case #{0}: {1}\n".format(case, solve(line.strip())))
		case += 1
	