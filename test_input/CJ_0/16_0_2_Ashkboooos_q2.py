def main():
	file_name = 'B-large.in'
	f = open(file_name , 'r')
	lines = f.read().splitlines()
	test_cases = int(lines[0])
	result = ''
	for i in xrange(1, test_cases + 1):
		line = lines[i]
		cur = line[0]
		switch = 0
		for s in line[1:]:
			if cur != s:
				switch += 1
				cur = s
		if line[-1] == '-':
			switch += 1
		r = "Case #" + str(i) + ": " + str(switch) + '\n'
		result += r
	print result
	f = open('q2.out', 'w')
	f.write(result)
	f.close()
if __name__ == '__main__':
	main()
