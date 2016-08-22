
import math
import sys
import itertools

def convert(s, bases):
    #nums = [int(x) for x in s]
    ret = []
    for base in bases:
        exp = 0
        ans = 0
        for i in reversed(s):
            if exp == 0:
                ans += i
            elif i == 0:
                pass
            else:
                ans += i * (base**exp)
            exp += 1
        ret.append(ans)
    return ret

def find_divisors(perm, bases):
    divisors = []
    nums = convert(perm, bases)
    index = 0
    for n in nums:
        if n < 4:
            #print "%d is prime: %s base %d" % (n, ''.join(map(str, perm)), bases[index])
            return None
        m = int(math.sqrt(n))
        found = False
        for i in xrange(2, m+1):
            if n % i == 0:
                divisors.append(i)
                found = True
                break
        if not found:
            #print "%d is prime: %s base %d" % (n, ''.join(map(str, perm)), bases[index])
            return None
        index += 1
    return divisors

def find_nums(elements, l, num, bases):
    results = {}
    for perm in itertools.product(elements, repeat=l - 2):
        perm = list(perm)
        perm.insert(0, 1)
        perm.insert(l, 1)
        divisors = find_divisors(perm, bases)
        if divisors is not None:
            results[''.join(map(str, perm))] = divisors
            if len(results) == num:
                break
    return results

bases = [2,3,4,5,6,7,8,9,10]
def solve(filename):
    with open(filename, 'r') as f:
        num_tests = int(f.readline())
        for i in xrange(num_tests):
            (l, num_coins) = map(int, f.readline().split())
            results = find_nums([0,1], l, num_coins, bases)
            assert len(results) == num_coins
            print "Case #%d:" % (i + 1)
            for (perm, divisors) in results.items():
                assert len(perm) == l
                assert len(divisors) == len(bases)
                print "%s %s" % (perm, " ".join(map(str, divisors)))


solve(sys.argv[1])
