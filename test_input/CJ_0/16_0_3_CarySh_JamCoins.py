__author__ = 'cary shindell'

opt = open("jc.out", 'w')
#opt2 = open("jc.jc", 'w')

N = 16
J = 50

def isPrime(n):
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    i = 5
    w = 2

    while i * i <= n and i < 5000000000:
        if n % i == 0:
            return i

        i += w
        w = 6 - w

    return 0

"""poss = ["0","1"]
jamcoins = []
for a in poss:
    for b in poss:
        for c in poss:
            for d in poss:
                for e in poss:
                    for f in poss:
                        for g in poss:
                            for h in poss:
                                for i in poss:
                                    for j in poss:
                                        for k in poss:
                                            for l in poss:
                                                for m in poss:
                                                    for n in poss:
                                                        jamcoins.append("1"+a+b+c+d+e+f+g+h+i+j+k+l+m+n+"1")

opt2.write(str(jamcoins))

opt2.close()"""

legitjc = []
jcdiv = []

for j in jamcoins:
    print j
    if len(legitjc) == 50:
        break
    div = []
    legit = True
    for base in range(2,11):
        bv = int(j, base)
        pp = isPrime(bv)
        if pp == 0:
            legit = False
            break
        else:
            div.append(pp)
    if legit:
        legitjc.append(j)
        jcdiv.append(div)

opt.write("Case #1:\n")
ctr = 0
for jc in legitjc:
    dastr = (" %d %d %d %d %d %d %d %d %d" % tuple(jcdiv[ctr]))
    opt.write(str(int(jc)) + dastr + "\n")
    ctr += 1

opt.close()