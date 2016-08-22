import os

N = 32
J = 500

f = open('out.txt', 'w')
f.write('Case #1:\n')

prime = [2, 3, 5, 7]

def primes():
    global prime
    i = 9
    while i < 1000000:
        for p in prime:
            if i % p == 0:
                break
            if p*p > i:
                prime.append(i)
                if len(prime) % 10000 == 0:
                    print len(prime), i
                break
        i = i + 2

def basen(val, base):
    global prime
    start = 1
    v = val
    basev = 0
    while v:
        if v & 1:
            basev += start
        start *= base
        v = v >> 1

    for p in prime:
        if basev % p == 0:
            return p

    return -1

primes()
    
numcoins = 0
val = 1 + pow(2, N - 1)
while numcoins < J:
    jamcoin = []
    found = True
    for i in range(0, 9):
        c = basen(val, i + 2)
        if c == -1:
            found = False
            break
        jamcoin.append(c)
    printval = ""
    v = val
    s = []
    while v:
        if v % 2:
            s.append('1')
        else:
            s.append('0')
        v  = v / 2
    sz = len(s)
    for i in range(0, sz):
        cc = s[sz - i - 1]
        printval = printval + cc
    if found:
        printval = printval + '***** %d' % (numcoins + 1)
        #printval = ""
        #v = val
        #s = []
        #while v:
        #    if v % 2:
        #        s.append('1')
        #    else:
        #        s.append('0')
        #    v  = v / 2
        sz = len(s)
        for i in range(0, sz):
            cc = s[sz - i - 1]
            f.write(str(cc))
            #printval = printval + cc
        #print printval
        for i in range(0, 9):
            f.write(' %d' % (jamcoin[i]))
        f.write('\n')
        numcoins = numcoins + 1
    print printval
    val += 2
    
f.close()