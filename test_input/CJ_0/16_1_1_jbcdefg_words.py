#!/usr/bin/python

import sys


if __name__ == '__main__':

    fname = sys.argv[-1]
    with open(fname, 'r') as f:
        lines = [l[:-1] for l in f.readlines()]

    outlines = []

    for i, line in enumerate(lines[1:]):
        out = ''
        for c in line:
            if not out:
                out = c
            elif c >= out[0]:
                out = c + out
            else:
                out = out + c
        outlines.append('Case #%s: %s' % (i + 1, out))

    fname = fname[:-2] + 'out'
    with open(fname, 'w') as f:
        outstr = '\n'.join(outlines)
        print outstr
        f.write(outstr)
