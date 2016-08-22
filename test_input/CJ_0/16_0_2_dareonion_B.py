#!/usr/bin/env python
import itertools
import sys

def number_flips(sequence):
    last_c = sequence[0]
    flips = 1
    for c in sequence:
        if c != last_c:
            flips += 1
            last_c = c
    if sequence[-1] == '+':
        return flips-1
    else:
        return flips
    
def main(argv=sys.argv):
    infile = argv[1]
    outfile = argv[2]
    cases = []
    with open(infile) as f:
        num_cases = int(f.readline())
        for _ in xrange(num_cases):
            cases.append(f.readline().strip())

    with open(outfile, 'w') as g:
        for i, c in enumerate(cases, 1):
            g.write("Case #{}: {}\n".format(i, number_flips(c)))
    return 0

if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)
