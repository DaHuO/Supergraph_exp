from sys import stdin, stdout

def solve(p):
    p = [pi=="+" for pi in p[::-1]]

    flips = 0
    ok = True
    for i in p:
        if i != ok:
            flips += 1
            ok = not ok

    return flips


T = int(stdin.readline())

for t in range(T):
    p = stdin.readline().strip()

    result = solve(p)

    stdout.write("Case #%d: %s\n"%(t+1, result))