
import sys

def flip(bottom, cakes):
    # 0 is top of stack
    #print "flip bottom: %d" % bottom
    new_top = cakes[:bottom]
    new_top = [x for x in reversed(new_top)]
    for index, value in enumerate(new_top):
        if new_top[index] == '+':
            new_top[index] = '-'
        else:
            new_top[index] = '+'

    new = new_top + cakes[bottom:]
    #print "after: %s" % ''.join(new)
    return new


def find_num_leading(c, cakes):
    res = 0
    for i in cakes:
        if i == c:
            res += 1
        else:
            break
    return res

def find_reverse(c, cakes):
    found = len(cakes) - 1
    while found >= 0:
        if cakes[found] == '-':
            break
        found -= 1
    return found

def do_flips(cakes):
    count = 0
    while True:
        base = find_reverse('-', cakes)
        if base == -1:
            return (count, cakes)

        num_leading = find_num_leading('-', cakes)
        if num_leading == base + 1:
            count = count + 1
            cakes = flip(base + 1, cakes)
            continue
        else:

            num_leading  = find_num_leading('+', cakes)
            if num_leading > 0:
                count += 1
                cakes = flip(num_leading, cakes)
            count += 1
            cakes = flip(base+1, cakes)

def solve(filename):
    with open(filename, 'r') as f:
        num_tests = int(f.readline())
        for i in xrange(num_tests):
            cakes = f.readline()
            cakes = list(cakes.strip())
            (count, cakes) = do_flips(cakes)
            for c in cakes:
                assert c == '+'

            print "Case #%d: %d" % (i + 1, count)

solve(sys.argv[1])
c = []
for i in range(50):
    c.extend(('-','+'))
