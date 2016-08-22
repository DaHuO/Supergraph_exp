#!/bin/python
def prime(n):
    n = int(n)
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
T = int(input())
for case in range(T):
    N, J = map(int,input().split())
    gen = [j for j in range(int(2**(N-1)),int(2**N))]
    o = {}
    for i in gen:
        if len(o) == J:
            break
        div = []
        temp = bin(i)[2:]
        if temp[-1] == '0':
            continue
        for j in range(2,11):
            inBase = int(temp,j)
            if prime(inBase):
                break
            k = 2
            while True:
                if inBase % k == 0:
                    div.append(k)
                    break
                k += 1
        if len(div) == 9:
            o[temp] = div
    o = list(o.items())
    print('Case #{}:'.format(case+1))
    for j in o:
        print(j[0] + ' ' + ' '.join(map(str,j[1])))
