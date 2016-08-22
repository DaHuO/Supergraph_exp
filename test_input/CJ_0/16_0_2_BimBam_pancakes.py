def truncate(pancakes):
    i = len(pancakes)
    while i > 0:
        if pancakes[i - 1]:
            i -= 1
        else:
            break
    return pancakes[:i]

def flip( p ):
    return [not x for x in p[::-1]]

def takeFromTop( p ):
    i = 0
    while i < len(p) and p[i]: i += 1
    return flip(p[:i]) + p[i:]
def flips( p ):
    cnt = 0
    while not all(p):
        p = truncate(p)
        cnt += 1
        if not p[0]:
            p = flip(p)
        else:
            p = takeFromTop(p)
    return cnt

def tests():
    print truncate([0, 1, 0, 0])
    print truncate([0])
    print truncate([1])
    print truncate([0,1,0,1,1])
    print flip([0, 1, 0, 1, 1])
    print flips([False])
    print flips([True])
    print flips([False, True])
    print flips([False, True, False])
    
with open("pancakesLarge.in", "rb") as f:
    nOfCases = int(f.readline().strip())
    for i in range(nOfCases):
        n = map(lambda x: x == '+' and True or False, f.readline().strip())
        s = flips(n)
        print "Case #{}: {}".format( i + 1, s )
