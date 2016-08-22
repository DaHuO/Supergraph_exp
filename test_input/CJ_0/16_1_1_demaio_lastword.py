#! /usr/bin/python

import sys
def solve(lines, idx):
    chars = [c for c in lines[idx]]
    ret = [chars[0]]
    chars = chars[1:]
    for c in chars:
        if c < ret[0]:
            # Append
            ret.append(c)
        else:
            ret.insert(0, c)
    return "".join(ret), 1

def main():
    fn = sys.argv[1] 
    with open(fn) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    t = int(lines[0])
    idx = 1
    for i in range(t):
        result, num_used = solve(lines, idx)
        idx += num_used
        print "Case #%d: %s" % (i+1, result)

if __name__ == "__main__":
    main()
