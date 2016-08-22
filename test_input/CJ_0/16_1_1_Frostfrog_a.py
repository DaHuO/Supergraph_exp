import sys


if __name__ == '__main__':
	T = int(sys.stdin.readline());
	cases = 1
	while T != 0: 
		T -= 1
		input = sys.stdin.readline()
		input = input.strip()
		l = []
		
		for alpha in input:
			if len(l) == 0 or alpha >= l[0]:
				l = [alpha] + l
			else:
				l.append(alpha)

		output = 'Case #{0}: {1}'.format(cases, ''.join(l))
		print(output)
		cases += 1

