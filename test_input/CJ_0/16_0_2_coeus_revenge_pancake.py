import fileinput

def solve(pancakes, n, target_char):
    if n > len(pancakes): return 0
    if pancakes[len(pancakes) - n:] == target_char:
        return solve(pancakes, n + 1, target_char)
    else:
        return 1 + solve(pancakes, n + 1, pancakes[len(pancakes) - n:])



def compress(pancakes):
    out = pancakes[0]
    cur = pancakes[0]
    for i in range(1, len(pancakes)):
        if pancakes[i] == cur:
            continue
        cur = pancakes[i]
        out += pancakes[i]
    return out


do_see_first = False
case = 1
for ln in fileinput.input():
    if not do_see_first:
        do_see_first = True
        continue
    data = ln.strip()
    data = compress(data)
    print "Case #%s: %s " % (case, solve(data, 1, "+"))
    case += 1
