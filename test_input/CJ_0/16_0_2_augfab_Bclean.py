#!/usr/bin/env python

import sys
import re

def flip_pstack(pstack):
    #import pdb; pdb.set_trace()
    retstring = ""
    for i in xrange(len(pstack)):
        retstring += "b" if pstack[-(i+1)] == "h" else "h"
    return retstring
    

def get_result(n, lstack, rstack):
    pstack = lstack + rstack
    if not ("b" in pstack):
        return n
    else:
        last_blanks = re.compile("^(h*)(.*?)(b+)(h*)$")
        m = last_blanks.match(pstack)
        if len(m.group(1)) != 0:
            lstack = flip_pstack(m.group(1))
            rstack = m.group(2) + m.group(3) + m.group(4)
        else:
            lstack = flip_pstack(m.group(1) + m.group(2) + m.group(3))
            rstack = m.group(4)
        return get_result(n+1, lstack, rstack)


def replace_plus_and_minus(s):
    """Replace "+" by h (happy) and "-" by b (blank)."""
    """Discard other characters."""
    retstring = ""
    for i in xrange(len(s)):
        if s[i] == "+":
            retstring += "h"
        elif s[i] == "-":
            retstring += "b"
    return retstring

def main():
    fh = open(sys.argv[1])
    fhout = open("out", "w")

    cases = int(fh.readline().strip())
    i = 0

    for i in xrange(1, cases+1):
        pstack = replace_plus_and_minus(fh.readline().strip())
        result = get_result(0, pstack, "")
        fhout.write("Case #{}: {}\n".format(i, result))

    fhout.flush()
    fh.close()
    fhout.close()
    sys.exit(0)

if __name__ == "__main__":
    main()
