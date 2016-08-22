
def solve(cakes):
    count = 0
    for i in xrange(len(cakes)):
        if cakes[i] == '-':
            count += 1
            for j in xrange(i, len(cakes)):
                if cakes[j] == '-':
                    cakes[j] = '+'
                else:
                    cakes[j] = '-'
                    
    return count


if __name__ == '__main__':
    n = int(raw_input())
    for i in xrange(n):
        cakes = raw_input()
        c = solve(list(cakes)[::-1])
        print "Case #{}: {}".format(i + 1, c)

            