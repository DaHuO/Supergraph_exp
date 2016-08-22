__author__ = 'cary shindell'

from copy import deepcopy

inp = open("pc.in", 'r')
opt = open("pc.out", 'w')

N = None
cases = []
for line in inp:
    if N is None:
        N = int(line)
    else:
        cases.append(str(line))

nc = []
for n in cases:
    if "\n" in n:
        nc.append(n[:-1])
    else:
        nc.append(n)

"""def flipx(stack, n):
    # flips the top n pancakes and returns new stack
    u = list(stack)
    s = u[:n]
    s.reverse()
    r = ""
    for p in s:
        if p == "+":
            r += "-"
        else:
            r += "+"
    r += stack[n:]
    return r"""

results = []

for c in nc:
    if "-" not in c:
        results.append(0)
    elif "+" not in c:
        results.append(1)
    else:
        s = deepcopy(c)
        while len(s) > 0 and s[-1] == "+":
            s = s[:-1]
        changes = 1
        sign = s[0]
        for x in s:
            if x != sign:
                changes += 1
                sign = x
        results.append(changes)

"""
for c in nc:
    if "-" not in c:
        results.append(0)
    elif "+" not in c:
        results.append(1)
    else:
        man = 0
        s = deepcopy(c)
        while len(s) > 0 and s[-1] == "+":
            s = s[:-1]
        while len(s) > 0 and s[-1] == "-":
            ncount = 0
            for x in s:
                if x == "-":
                    ncount += 1
                else:
                    break
            if ncount == len(s):
                man += 1
                s = flipx(s, len(s))
                break
            pcount = 0
            pnum = 0
            ctr2 = 0
            for x in s:
                if x == "+":
                    pc = 1
                    ctr3 = 0
                    while s[ctr2+ctr3+1] == "+":
                        ctr3 += 1
                        pc += 1
                    if pc > pcount:
                        pcount = pc
                        pnum = ctr2 + 1 + ctr3
                ctr2 += 1
            #print c, pcount, pnum, ncount
            if s[0] == "-":
                if pcount > ncount:
                    man += 2
                    s = flipx(s, pnum)
                    s = flipx(s, len(s))
                    while len(s) > 0 and s[-1] == "+":
                        s = s[:-1]
                else:
                    man += 1
                    s = flipx(s, len(s))
                    while len(s) > 0 and s[-1] == "+":
                        s = s[:-1]
            else:
                man += 1
                s = flipx(s, pnum)
                while len(s) > 0 and s[-1] == "+":
                    s = s[:-1]
            if s[0] == "-":
                man += 1
                s = flipx(s, len(s))
                while len(s) > 0 and s[-1] == "+":
                    s = s[:-1]
            else:
                ctr = -1
                num = 0
                for x in s:
                    if x == "+" and s[ctr] == "-":
                        num += 1
                        ctr -= 1
                    else:
                        break
                man += 2
                s = flipx(s, num)
                s = flipx(s, len(s))
                while len(s) > 0 and s[-1] == "+":
                    s = s[:-1]
        results.append(man)
"""

CTR = 1
for x in results:
    opt.write("Case #" + str(CTR) + ": " + str(x) + "\n")
    CTR += 1

inp.close()
opt.close()
