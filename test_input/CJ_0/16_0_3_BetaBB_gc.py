
# return 0 if prime
def isPrime(n, s):
    # print "isPrime", n
    # for i in xrange(2,int(n**0.5)+1):
    for i in s:
    	# print i
        if n%i==0 and n != i:
            return i

    return 0


def generateNum(idx, base):
	ret = 0
	curBase = 1
	while idx:
		ret += idx % 2 * curBase
		curBase *= base
		idx /= 2
	return ret

def toBinary(n, leng):
	ret = ""
	while n > 0:
		ret = str(n % 2) + ret
		n /= 2

	if len(ret) < leng:
		ret = '0' * (leng - len(ret)) + ret

	print ret
	return ret

def calculate(n, j):
	i = 2**(n-1) + 1
	# i = 0
	cases = 0
	ret = ""
	s = gen_primes()
	while 1:
		out = ""
		if cases >= j:
			break
		suc = True
		out += toBinary(i, n)

		for base in range(2, 11):
			num = generateNum(i, base)
			div = isPrime(num, s)
			# div = 1
			# print num, div
			if div == 0:
				suc = False
				break
			else:
				out += " " + str(div)
				# s.add(div)

		i += 2
		if suc:
			cases += 1
			ret += out + "\n"
			# print "out: ", out

	# print ret
	return ret

def main():
    inpfile = open("C-large.in", 'r')
    outfile = open('outfile', 'w')
    casenum = int(inpfile.readline().strip())
    for case in range(1, casenum + 1):
        line = inpfile.readline().strip()
        linelst = line.split()
        N = int(linelst[0])
        J = int(linelst[1])

        # print N, J
        ret = calculate(N, J)


        result = "Case #" + str(case) + ":\n" + ret
        print result
        outfile.write(result)
    inpfile.close()
    outfile.close()


def gen_primes():
    n = 2
    primes = set()
    pl = []
    for i in range(2**16):
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.add(n)
            pl.append(n)
            
            # yield n
        n += 1
    print pl
    return pl



if __name__ == "__main__":
	main()
    # print generateNum(35, 4)
    # print toBinary(6, 16)

    # gen_primes()


