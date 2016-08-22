from __future__ import print_function
import math

N = 32
J = 500

def divisor(n):
    i = 3
    targ = min(math.trunc(math.sqrt(n))+1, 100000)
    while i < targ:
        if n % i == 0:
            return i
        i += 2
    return 1


def convertTo(num, base):
    ans = 0
    mult = 1
    for c in num[::-1]:
        ans += int(c)*mult
        mult *= base
    return ans

f1 = open('D:\output.txt', 'w')
n = pow(2, N-1)+1
t = pow(2, N)
cnt = 0
f1.writelines("Case #1:\n")
while n < t and cnt < J:
    s = "{0:b}".format(n)
    B = []
    for a in range(2, 11):
        tmp = convertTo(s, a)
        d = divisor(tmp)
        if d > 1:
            B.append(d)
        else:
            break
    n += 2
    if len(B) < 9:
        continue
    f1.writelines(s + " " + ' '.join(str(num) for num in B)+"\n")
    #print s, ' '.join(str(num) for num in B)
    cnt += 1
