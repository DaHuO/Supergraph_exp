from sys import *

def divisor(n):
    c = 2
    while c * c <= n:
        if n % c == 0:
            return c
        c += 1
    return -1

def convert(s, k, max_len):
    ans = 0
    for i in range(max_len):
        if (2 ** i) & s:
            ans += k ** i
    return ans

def binary(n, max_len):
    ans = ""
    while n:
        ans += str(n % 2)
        n //= 2
    while len(ans) < max_len:
        ans += '0'
    return ans[::-1]

fin = open("c.in", "r")
fout = open("c.out", "w")

t = int(fin.readline())
for i in range(1, t + 1):
    print("Case #", i, ":", sep = '', file = fout)
    max_len, am = map(int, fin.readline().split())
    i = 2 ** (max_len - 1) + 1
    cnt = 0
    while i < 2 ** max_len and cnt < am:
        s = binary(i, max_len)
        ans = []
        for j in range(2, 11):
            ans.append(divisor(convert(i, j, max_len)))
        if ans.count(-1) == 0:
            cnt += 1
            print(s, ' '.join(map(str, ans)), file = fout)
        i += 2
        
fout.close()