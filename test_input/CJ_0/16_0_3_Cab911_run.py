
import math

def find_primes():
    a = []
    t = 5
    a.append(3)
    while len(a) < 1000:
        prime = True
        i = 0
        num = a[i]
        while prime and num < math.sqrt(t):
            if (t % num) == 0:
                prime = False
            num = a[i]
            i += 1
        if prime:
            a.append(t)
        t += 2
    return a

primes = find_primes()

def first_divider(num):
    i = 0    
    while i < len(primes) and primes[i] < math.sqrt(num):
        if (num % primes[i]) == 0:
            return primes[i]
        i += 1
    return 0


class Iter:
    def __init__(self, n):
        self.n = n
        Iter.seed = int('1'+'1'.zfill(n-1), 2)
    def next_num(self):
        valid = False
        Iter.seed += 1
        while not valid:
            s = bin(Iter.seed)[2:].zfill(self.n)
            if s[0] == '1' and s[-1] == '1':
                valid = True
            Iter.seed += 1
        return s

def get_dividers(b, d):
    for i in range(2, 11):
        f = first_divider(int(b, i))
        if f == 0:
            return False
        d.append(f)
    return True


raw_input()
l = raw_input()
(w, n) = l.split()
w = int(w)
n = int(n)

iter = Iter(w)
cnt = 0
print "Case #1:"
while cnt < n:
    b = iter.next_num()
    d = []
    if get_dividers(b, d):
        s = ""
        for i in d:
            s = s + " " + str(i)
        print "%s%s" %(b, s)
        cnt += 1


