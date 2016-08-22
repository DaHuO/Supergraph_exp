import sys


def sol(S):
    res = ''
    for c in S:
        if res+c < c+res:
            res = c+res
        else:
            res = res+c
    return res

inp = open(sys.argv[1])
out = open(sys.argv[2], 'w')
T = int(inp.readline())
for i in range(T):
    S = inp.readline().strip()
    out.write("Case #{}: {}\n".format(i+1, sol(S)))
inp.close()
out.close()