class Prime:
    def __init__(self, N = 70000):
        self.primes = []
        self.max = N
        for i in range(2, N):
            prime = True
            for x in self.primes:
                if x * x > i:
                    break
                elif i % x == 0:
                    prime = False
                    break
            if prime:
                self.primes.append(i)

    def getdivisor(self, n):
        for x in self.primes:
            if x * x > n:
                return 0
            elif n % x == 0:
                return x
        x = self.primes[-1] + (self.primes[-1] % 2)
        while x * x <= n:
            if n % x == 0:
                return x
            x += 2
        return 0
            
def solve():
    n, j = map(int, raw_input().strip().split())
    res = []
    p = Prime()
    if n >= 2:
        i = 0
        while len(res) < j and i <= (1<<(n - 2))-1:
            coin = '1' + format(i, "0%db" % (n-2)) + '1'
            divisors = []
            for b in range(2, 10 + 1):
                num = p.getdivisor(int(coin, b))
                # print num, coin, b
                if num == 0:
                    break
                divisors.append('%d' % num)

                    
            if len(divisors) == 9:
                res.append((coin, divisors))
            i += 1
    else:
        pass
    for i, j in res:
        print i, ' '.join(j)

T = int(raw_input())

for t in range(1, T+1):
    print "Case #%d:" %t
    solve()
