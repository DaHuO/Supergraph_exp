import sys, math
inp = open("in.txt")
out = open("out.txt","w+")
sys.stdout = out
tc = 0

class ImpossibleError(Exception):
	pass

t = int(inp.readline())

def print_case(case, result):
    debug("Case #%d: %s" % (case, str(result)))
    print "Case #%d: %s" % (case, str(result))

def debug(message):
	if len(sys.argv) > 1 and sys.argv[1] == "silent":
		return
	sys.stdout = sys.__stdout__
	print message
	sys.stdout = out

prime_cache = {}
def is_prime(n):
    if n in prime_cache:
        return prime_cache[n]
    if n % 2 == 0 and n > 2: 
        prime_cache[n] = (False, 2)
        return False, 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            prime_cache[n] = (False, i)
            return False, i
    prime_cache[i] = (True, 0)
    return True, 0


for tc in xrange(t):
    n, j = [int(x) for x in inp.readline().split()]
    print_case(tc+1, "")
    found = 0
    for i in xrange(2**(n-1)+1, 2**n, 2):
        s = bin(i)[2:]
        
        if s[0] != "1" or s[-1] != "1":
            continue
        
        factors = []
        broken = False
        for b in xrange(2, 11):
            k = int(s, b)
            prime, factor =  is_prime(k)
            if prime:
                broken = True
                break
            factors.append(factor)
        if not broken:
            found += 1
            print s, " ".join(map(str, factors))
            debug(found)
        if found == j:
            break
        