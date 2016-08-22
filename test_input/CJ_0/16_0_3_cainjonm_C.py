import sys
import random

def to_base_10(num, from_base):
    cur = 1
    ret = 0
    for x in reversed(num):
        val = int(x)
        ret += val * cur
        cur *= from_base
    return ret

def rand_str(l):
    st = []
    for x in range(l):
        st.append(random.choice('01'))
    return ''.join(st)

def find_divisor(num):
    for x in range(2, 10000):
        if num % x == 0 and x != num:
            return x
    return None

def generate(N):
    while True:
        st = '1' + rand_str(N - 2) + '1'
        divisors = []
        fail = False
        for x in range(2, 11):
            num = to_base_10(st, x)
            divisor = find_divisor(num)
            if divisor == None:
                fail = True
                break
            divisors.append(divisor)
        if not fail:
            return (st, divisors)


T = int(input())
for t in range(1, T+1):
    N, J = [int(x) for x in input().split()]
    print("Case #{0}:".format(t))
    res = []
    L = 0
    while len(res) != J:
        x = generate(N)
        print("generated", L, "so far", file=sys.stderr)
        L+=1
        res.append(x)

    for x in res:
        print(x[0],end=' ')
        for divisor in x[1]:
            print(divisor,end =' ')
        print('')
