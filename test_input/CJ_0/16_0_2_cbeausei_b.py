import sys

T = int(input())
for N in range(1, T + 1):
    out = 'Case #' + str(N) + ': '
    s = input()
    n = len(s)
    nb = 0
    v = s[0]
    for w in s:
        if w != v:
           nb += 1
           v = w
    if s[len(s) - 1] == '-':
        nb += 1
    out += str(nb) + '\n'
    sys.stdout.write(out)
    sys.stdout.flush()
    sys.stderr.write(out)
    sys.stderr.flush()