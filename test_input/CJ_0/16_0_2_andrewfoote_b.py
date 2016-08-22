num = int(raw_input())

def solve(s):
    state = '+'
    x = 0
    s = list(s)
    s = s[::-1]
    for c in s:
        if c != state:
            x += 1
            state = c
    return x

for i in range(1, num+1):
    n = solve(raw_input())
    print "Case #{}:".format(i), n


