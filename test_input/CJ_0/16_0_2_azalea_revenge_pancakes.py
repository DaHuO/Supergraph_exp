#!/usr/bin/python


def get_flip_number(s):
    s = s.rstrip('+')  # remove trailing '+'
    if not s:
        return 0
    incremental = 1 if s.startswith('-') else 0
    s = s.lstrip('-')
    if not s:
        return 1
    # for every '+-' need 2 flips
    return incremental + 2 * (len(s.split('+-')) - 1)

if __name__ == '__main__':
    import sys
    infile = sys.argv[1]
    f = open(infile)
    T = int(f.readline().strip())
    for i in range(T):
        line = f.readline().strip()
        print 'Case #%d: %s' % (i + 1, get_flip_number(line))
