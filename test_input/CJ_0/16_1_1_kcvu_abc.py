#!/usr/bin/env python

def best_order(org_str):
    result = org_str[0]
    for c in org_str[1:]:
        if c < result[0]:
            result += c
        else:
            result = c + result
    return result

if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as infile:
        _ = infile.readline()
        line_index = 0
        for line in infile:
            line_index += 1
            print "Case #%d: %s" % (line_index, best_order(line.strip()))