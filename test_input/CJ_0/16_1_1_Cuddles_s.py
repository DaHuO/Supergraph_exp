import sys
from collections import defaultdict


def print_solutions(filename):
    content = open(filename).read().strip().split('\n')
    test_case_count = int(content[0])
    i = 1
    while i <= test_case_count:
        w = content[i]
        nw = w[0]
        for l in w[1:]:
            if l >= nw[0]:
                nw = l + nw
            else:
                nw = nw + l
        print("Case #%s: %s" % (i, nw))
        i += 1

filename = sys.argv[1]
print_solutions(filename)
