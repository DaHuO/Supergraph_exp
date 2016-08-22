import sys
import math

def sieve(n):
    s = [True] * n
    for i in range(n):
        if s[i]:
            pass

def is_jam(l):
    dl = []
    for i in l:
        div = False
        for j in range(2,int(math.sqrt(i)+1)):
            if i % j == 0:
                dl.append(j)
                div = True
                break
        if not div:
            return None
    return dl

def get_num(s):
    num = []
    for i in range(2, 11):
        sumi = 0 
        for d in s:
            sumi*=i
            sumi+=1 if d == '1' else 0
        num.append(sumi)
    return num 

def main():
    n = 16
    j = 50
    l = [0] * 9
    for i in range(2,11):
        l[i-2] = 1 + i**(n-1)

    fl = []
    while j > 0:
        dl = is_jam(l)
        if dl is not None:
            j-=1
            dl.insert(0, l[-1])
            fl.append(dl)
        l = get_num(bin(l[0] + 2)[2:])

    print("Case #1:")
    for i in fl:
        print(*i)

main()
