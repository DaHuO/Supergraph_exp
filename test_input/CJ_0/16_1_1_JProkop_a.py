num_problems = int(raw_input())

def solve(s):
    it = ''
    for a in s:
        if not it:
            it = a
        else:
            pos1 = a + it
            pos2 = it + a
            if pos1 > pos2:
                it = pos1
            else:
                it = pos2
    return it

for x in range(num_problems):
    s = str(raw_input())
    soln = solve(s)
    print 'Case #{}: {}'.format(x + 1, soln)
