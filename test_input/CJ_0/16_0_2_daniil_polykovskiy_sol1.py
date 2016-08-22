import sys


def sol(S):
    r = 0
    for i in range(len(S)-1):
        if S[i] != S[i+1]:
            r += 1
    if S[-1] == '-':
        r += 1
    return r

inp = open(sys.argv[1])
out = open(sys.argv[2], 'w')
T = int(inp.readline())
for i in range(T):
    S = inp.readline().strip()
    out.write("Case #{}: {}\n".format(i+1, sol(S)))
inp.close()
out.close()