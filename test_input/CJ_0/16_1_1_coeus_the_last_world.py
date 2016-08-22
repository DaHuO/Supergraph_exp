import fileinput 

def solve(s):
    out = [s[0]]
    for c in s[1:]:
        if c >= out[0]:
            out.insert(0, c)
        elif c < out[0]:
            out.append(c)
    return "".join(out)

do_see_first = False
case = 1
for ln in fileinput.input():
    if not do_see_first:
        do_see_first = True
        continue
    data = ln.strip()
    print "Case #%s: %s" % (case, solve(data))
    case += 1
