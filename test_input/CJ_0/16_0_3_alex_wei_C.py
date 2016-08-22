import sys
from random import randint

def is_prime(x):
    return x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0

def get_factor(x):
    if x % 2 == 0: return 2
    if x % 3 == 0: return 3
    if x % 5 == 0: return 5
    if x % 7 == 0: return 7
    return 0

def to_base(s, b):
    r, p = 0, 1
    for c in reversed(s):
        r += p * (ord(c) - ord('0'))
        p *= b
    return r

print('Case #1:')
T = int(input())
N, J = map(int, input().split())

k = 2 ** (N - 1) + 1
while J > 0:
    s = bin(k)[2:]
    ok = True
    for i in range(2, 11):
        if is_prime(to_base(s, i)):
            ok = False
            break
    if ok:
        w = [get_factor(to_base(s, i)) for i in range(2, 11)]
        if min(w) > 0:
            J -= 1
            print(s,' '.join(map(str,w)))
    k += 2
