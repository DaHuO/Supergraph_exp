import sys

def prime(n):
    if n%2 == 0:
        return 2
    for i in xrange(3, int(n**.5)+1, 2):
        if n%i==0:
            return i

    return None

def check(coin):
    divs = []
    for base in range(2, 11):
        p = 0
        tcoin = coin
        tnum = 0
        while tcoin>0:
            tnum += tcoin%2*base**p
            tcoin /= 2
            p += 1
        div = prime(tnum)
        if div is not None:
            divs.append(div)

    if len(divs) == 9:
        return divs
    else:
        return None

def binary(coin):
    res = ''

    tcoin = coin
    while tcoin > 0:
        res = str(tcoin%2) + res
        tcoin /= 2

    return res

def solve():
    res_count = 0
    print "Case #1:"
    for coin in xrange(2**15+1, 2**16, 2):
        divs = check(coin)
        if divs is not None:
            res_count += 1
            print binary(coin),
            for div in divs:
                print div,
            print
            if res_count == 50:
                break

if __name__=='__main__':
    solve()
