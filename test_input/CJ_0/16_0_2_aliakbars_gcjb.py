def pancakes(x):
    i = 0
    while set(x) != set('+'):
        if x[0] == '+':
            x = flip(x, x.find('-'))
        else:
            if x.find('+') == -1:
                i += 1
                break
            else:
                x = flip(x, x.find('+'))
        i += 1
    return i

if __name__ == '__main__':
    i = 1
    with open(sys.argv[1]) as f:
        f.readline()
        for line in f:
            val = line.strip()
            print 'Case #%d: %d' % (i, pancakes(val))
            i += 1