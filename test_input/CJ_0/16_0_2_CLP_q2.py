with open('input.large') as f:
    lines = (l.strip() for l in f.readlines()[1:])

def reducer(previous, next):
    symbol, total = previous
    total += symbol != next
    return next, total

for n, l in enumerate(lines, 1):
    _, total = reduce(reducer, l, (l[0], l[-1] == '-'))
    print 'Case #{}: {}'.format(n, total)
