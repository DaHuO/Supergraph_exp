def count(state):
    # digits = set([str(i) for i in range(10)])
    # index = 1
    # multiple = N
    c = 0
    while '-' in state:
        first = state[0]
        opposite = "+" if first == "-" else "-"
        pancakes = state.split(opposite)
        top_batch = pancakes[0]
        new_top_batch = opposite * len(top_batch)
        pancakes[0] = new_top_batch
        state = opposite.join(pancakes)
        c += 1

    return str(c)

if __name__ == '__main__':
    case = 'B-large'
    inp = open('%s.in'%case);
    out = open('%s.out'%case, 'w');

    cases = int(inp.readline())
    for i in xrange(1, cases + 1):
        state = inp.readline().strip()
        o = "Case #%d: %s"%(i, count(state))
        print o
        out.write('%s'%o)
        if i < cases:
            out.write('\n')
