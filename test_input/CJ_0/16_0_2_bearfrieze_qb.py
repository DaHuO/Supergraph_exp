import fileinput

def solve(N, answer):
    if all(N): return answer
    for i in reversed(range(len(N))):
        if not N[i]:
            for j in range(0, i + 1):
                N[j] = not N[j]
            break
    return solve(N, answer + 1)

def parse(S):
    N = []
    for c in S:
        if c == '-': N.append(False)
        if c == '+': N.append(True)
    return N

f = fileinput.input()
T = int(f.readline())

for case in range(1, T + 1):
    S = f.readline().strip('\n')
    print('Case #%d: %s' % (case, solve(parse(S), 0)))
