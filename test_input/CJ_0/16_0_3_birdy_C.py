def isprime(number):
    for num in xrange(2, int(number**0.5) + 2):
        if number % num == 0:
            return False
    return True

def convert_base(S):
    S = [c for c in S]
    all_base = []
    for m in range(2,11):
        total = 0
        for i in range(len(S)):
            if S[i] == '1':
                total += m**(len(S)-1-i)
        if isprime(total):
            return "...."
        all_base.append(total)
    return all_base

def devisor(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return i

def devisors(l):
    total = []
    for i in l:
        total.append(devisor(i))
    return total

import itertools
def solve(n,j):
    s = ['1']*n
    choices = [s]
    for i in xrange(1,n):
        for pos in itertools.combinations(range(n-2), i):
            s = ['1']*n
            for p in pos:
                s[p+1] = '0'
                if s not in choices:
                    choices.append(s)
    all_base = []
    for choice in choices[:j+6]:
        choice = ''.join(choice)
        if convert_base(choice) != "....":
            all_base.append(convert_base(choice))
    res = 0
    for base in all_base:
        res = devisors(base)
        print base[-1], ' '.join(str(x) for x in res)

def c():
    T = int(raw_input())
    for t in range(1,T+1):
        n,j = map(int,raw_input().split())
        print "Case #{}:".format(t), solve(n,j)

if __name__ == '__main__':
    c()
