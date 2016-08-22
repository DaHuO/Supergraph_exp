import itertools
import sys

def get_non_trivial_div_under_k(n, k):
    d = 2
    while (d*d <= n and d <= k):
        if n % d == 0:
            return d
        else:
            d += 1
    return 0

n = int(sys.argv[1])
j = int(sys.argv[2])

n -= 2
print("Case #1:")
jth = 0
k = 100
for i in range(0, 2**n):
    s=bin(i)[2:]
    s='0'*(n-len(s))+s
    jamcoin = '1' + s + '1'
    divs = []
    
    for base in range(2, 11):
        cur = int(jamcoin, base)
        div = get_non_trivial_div_under_k(cur, k)
        if div:
            divs.append(div)
        else:
            break
    
    if len(divs) == 9:
         jth += 1
         divs_str = ' '.join(list(map(str, divs)))
         print("%s %s" % (jamcoin, divs_str))
         if jth == j:
             break
