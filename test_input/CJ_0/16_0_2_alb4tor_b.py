#!/usr/bin/python

def op(i):
    out = []
    for l in i:
        if l == "+":
            out.append("-")
        else:
            out.append("+")
    out.reverse()
    return "".join(out)


def retourne(p, i):
    s1 = p[:i+1]
    s2 = p[i+1:]

    print "r", op(s1), s2

    return op(s1)+s2


nb = int(raw_input())

for n in xrange(1, nb+1):
    pile = raw_input()

    flip = 0
    last = pile[0]
    for i in pile[1:]:
        if i != last:
            flip += 1
            last = i

    if last == "-":
        flip += 1

    print "Case #%i:" % (n), flip
