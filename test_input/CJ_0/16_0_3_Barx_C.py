import math

class NoResult(Exception): pass

def brute(num):
	for i in xrange(2,int(math.pow(num,0.5))):
		if num % i == 0:
			return str(i)
	raise NoResult()



def solve(N, J):
	results = []
	s = "1" + "0"*(N-2) + "1"
	start = int(s, 2)
	
	while len(results) < J:
		r = []
		try:
			test_s = '{0:b}'.format(start)
			res =  [brute(int(test_s,x)) for x in xrange(2,11)]
			results.append("%s %s"%(test_s, " ".join(res)))
			
		except NoResult:
			pass
		start += 2
	
	return "\n".join(results)

def main(source, dest):
    with open(source, 'r') as fd, open(dest, 'w') as fo:
		T = int(fd.readline())
		N, J = fd.readline().rstrip().split(' ')
		results = solve(int(N),int(J))
		print "Case #1:"
		print results
		fo.write("Case #1:\n")
		fo.write(results)


if __name__ == "__main__":
	filename = os.path.basename(sys.argv[1])
	source = sys.argv[1]
	dest = os.path.join(sys.argv[2], filename.replace(".in.txt",".out.txt"))
	main(source, dest)