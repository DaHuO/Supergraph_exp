import sys

def readFile(fname):
	data = []
	with open(fname, 'r') as f:
		N = int(f.readline())
		print N
		for i in range(N):
			x = f.readline().rstrip()
			data.append(x)
	return data


def process(data):
	out = []
	for x in data:
		xout = x[0]
		for ch in x[1:]:
			if ch >= xout[0]:
				xout = ch + xout
			else:
				xout = xout + ch
		out.append(xout)
	return out

def output(fname, out):
	with open(fname, 'w') as f:
		for i, y in enumerate(out):
			f.write('Case #%d: %s\n' % (i+1, y))

if __name__ == '__main__':
	data = readFile(sys.argv[1])
	out = process(data)
	output(sys.argv[2], out)