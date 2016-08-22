import itertools

t = 40

cl = [10,3,10,10]

operations = ["+", "-", "*", "/"]

def r(a,b,o):
    a = float(a)
    b = float(b)

    if o == "*":
        return a*b
    elif o == "-":
        return a-b
    elif o == "+":
        return a+b
    elif o == "/":
        if b == 0:
            return -1000
        return a/b

for c in itertools.permutations(cl, 4):
    for o1 in operations:
        for o2 in operations:
            for o3 in operations:
                # single bracket
                b = c[0]
                b = r(b, c[1], o1)
                b = r(b, c[2], o2)
                b = r(b, c[3], o3)
                if b == t:
                    print str(c[0]) + o1 + str(c[1]) + o2 + str(c[2]) + o3 + str(c[3])

                # 2 bracket
                b1 = r(c[0],c[1], o1)
                b2 = r(c[2],c[3], o3)
                b = r(b1,b2,o2)

                if b == t:
                    print "(" + str(c[0]) + o1 + str(c[1]) + ")" + o2 + "(" + str(c[2]) + o3 + str(c[3]) + ")"
