def write_lastword(s):
    n = [s[0]]
    for c in s[1:]:
        if c >= n[0]:
            n = [c] + n
        else:
            n.append(c)
    return ''.join(n)

def test():
    print countsheep(0)
    print countsheep(1)
    print countsheep(2)
    print countsheep(11)
    print countsheep(1692)


def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        s = raw_input()
        lw = write_lastword(s)
        print "Case #{}: {}".format(i, lw)

if __name__=='__main__':
    main()
