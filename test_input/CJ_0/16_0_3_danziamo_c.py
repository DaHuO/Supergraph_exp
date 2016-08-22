import math

test_cases = int(raw_input())

l = []


def generate_primes():
    n = int(math.sqrt(math.pow(2, 32)))
    nums = set(range(n, 1, -1))
    while nums:
        p = nums.pop()
        l.append(p)
        nums.difference_update(set(range(p * 2, n + 1, p)))

generate_primes()

for case in xrange(1, test_cases + 1):
    print 'Case #1:'
    n, o = [int(i) for i in raw_input().split()]
    a = int(math.pow(2, n - 1))
    count = 0
    for i in xrange(a + 1, a * 2 + 1, 2):
        u = []
        b = bin(i)[2:]
        u.append(b)
        for j in xrange(2, 11):
            t = int(b, j)
            sq = int(math.sqrt(t))
            for k in l:
                if t % k == 0:
                    u.append(str(k))
                    break
                elif k > sq:
                    break
            if len(u) < j:
                break

        if len(u) == 10:
            count += 1
            print ' '.join(u)
            if count == o:
                break
    #print "Case #{}: {}".format(case, n)
