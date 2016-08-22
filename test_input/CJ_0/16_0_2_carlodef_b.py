def solve(l):
    if l:
        if l[-1]:
            return solve(l[:-1])
        else:
            if l[0]:
                for i, x in enumerate(l):
                    if x:
                        l[i] = False
                    else:
                        break
                return 1 + solve(l)
            else:
                return 1 + solve([not a for a in l][::-1])
    return 0


if __name__ == '__main__':
    T = int(raw_input())
    for i in xrange(T):
        l = [x == '+' for x in raw_input()]
        print "Case #%d: %d" % (i+1, solve(l))
