def main():
	f = open('B-large.in')
	cases = []
	for i in range(int(f.readline())):
		cases.append(list(f.readline()))
	
	f = open('b.out', 'w')
	for i in enumerate(cases):
		f.write("Case #%s: " % str(i[0]+1) + str(solve(list(i[1])))+'\n')


def solve(line):
	check = line[0]
	counter = 0
	pos = 0
	while '-' in line:
		while line[pos] == line[pos+1]:
			pos +=1
			if pos + 1 == len(line):
				if '-' in line:
					counter += 1
					return counter	
				else:
					return counter	 
		line = list(reversed(line[:pos+1])) + line[pos+1:]
		for i in range(pos+1):
			if line[i] == "+":
				line[i] = "-"
			else:
				line[i] = "+"
		counter += 1
		pos = 0

	return counter

if __name__ == '__main__':
	main()