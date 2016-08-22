from sys import argv
if __name__ == "__main__":
	inf = open(argv[1], 'r')
	lines = inf.readlines()
	inf.close()
	T = int(lines[0][:-1])
	ouf = open(argv[2], 'w')
	for i in range(1, T+1):
		line = lines[i][:-1]+'+'
		c = line[0]
		ans = 0
		for ch in line:
			if c != ch:
				ans += 1
				c = ch
		ouf.write("Case #%d: %d\n"%(i, ans))
	ouf.close()