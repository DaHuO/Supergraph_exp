import fileinput


def solve(inp):
    ret = ""
    for c in inp:
        if not ret:
            ret += c
        else:
            if c >= ret[0]:
                ret = c + ret
            else:
                ret += c
    return ret

for i, line in enumerate(fileinput.input()):
    if i == 0:
        continue
    line = line.strip()
    res = solve(line)
    print "Case #%d: %s" % (i, res)
