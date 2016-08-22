import sys
import string
def trace(f):
	indent = '    '
	trace.level = -1
	def _f(*args):
		trace.level += 1
		txt = '===>%s(%s)' % (f.__name__, map(repr, args))
		print indent*trace.level + txt
		try:
			result = f(*args)
			txt2 = '<===%s(%s) : %s' % (f.__name__, map(repr, args), str(result))
			print indent*trace.level + txt2
		finally:
			trace.level -= 1
		return result
	return _f

def readFile(fname):
	data = []
	with open(fname, 'r') as f:
		N = int(f.readline())
		print N
		for i in range(N):
			x = f.readline()
			x = x.translate(string.maketrans('-+', '01'))
			x = x.rstrip().rstrip('1')
			data.append(x)
	return data


def process(data):
	out = []
	memory = {'': 0, '0': 1, '1': 0}
	for x in data:
		sol = solve(x, memory)
		out.append(sol)
	return out

const = pow(2, 100) -1
#@trace
def solve(prob, memory):
	if prob in memory:
		return memory[prob]
	else:
		a = prob.rfind('1')
		if a == -1:
			return 1
		
		temp = (bin(int(prob[a+1:], 2) ^ const)[a+1-len(prob):])[::-1]

		newprob = temp + prob[:a+1]
		newprob = newprob.rstrip('1')

		sol1 = 2 + solve(newprob, memory)

		sol2 = 10000000000000
		if prob[0] == '0':
			newprob2 = (bin(int(prob, 2) ^ const)[2:])[::-1]
			newprob2 = newprob2.rstrip('1')
			sol2 = 1 + solve(newprob2, memory)

		sol = min(sol1, sol2)
		
		memory[prob] = sol
		return sol


def output(fname, out):
	with open(fname, 'w') as f:
		for i, y in enumerate(out):
			f.write('Case #%d: %s\n' % (i+1, y))

if __name__ == '__main__':
	data = readFile(sys.argv[1])
	out = process(data)
	#print out
	output(sys.argv[2], out)