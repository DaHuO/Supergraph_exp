#!/usr/bin/python

import sys

def isprime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return i
        i += 1
    return None

def check(arr):
    ans = []
    for k in arr:
        res = isprime(k)
        if res is not None:
            ans.append(str(res))
        else:
            return None
    return ans

def generate(N, i):
    a2 = (1 << (N - 1)) + 1 + (i << 1)
    arr = [0] * N
    for k in range(N):
        a2, arr[k] = a2 // 2, a2 % 2
    ans = []
    for j in range(2, 11):
        num = 0
        for k in range(N - 1, -1, -1):
            num *= j
            num += arr[k]
        ans.append(num)
    return ans

T = int(input())
for t in range(T):
    N, J = map(int, input().split())
    i = 0
    print('Case #{}:'.format(t + 1))
    while J != 0:
        arr = generate(N, i)
        i += 1

        ans = check(arr)
        if ans is not None:
            print('{} {}'.format(arr[-1], ' '.join(ans)))
            J -= 1

