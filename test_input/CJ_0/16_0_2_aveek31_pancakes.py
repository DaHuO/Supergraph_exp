
import math

def nlz(i, t):
    if not i: return 32
    n = 0
    if i <= 0x0000FFFF:
        n = n +16
        i = i <<16
    if i <= 0x00FFFFFF:
        n = n + 8;
        i = i << 8
    if i <= 0x0FFFFFFF:
        n = n + 4
        i = i << 4
    if i <= 0x3FFFFFFF:
        n = n + 2
        i = i << 2
    if i <= 0x7FFFFFFF:
        n = n + 1
    return (n + t) - 32

def nlo(i,t):
    return nlz(int(math.pow(2, t)-1) - i,t)

def pancakes(s):
    s = ''.join(map(lambda x: '1' if x == '+' else '0', list(s)))
    cur_ops = 0
    n = len(s)
    while nlo(int(s,2), n) != 32:
        if nlz(int(s,2), n):
            s = s.replace('0', '1', nlz(int(s,2), n))
            cur_ops += 1
        elif nlo(int(s,2), n):
            s = s.replace('1', '0', nlo(int(s,2), n))
            cur_ops += 1
    return cur_ops


if __name__ == "__main__":
    import fileinput
    f = fileinput.input()

    T = int(f.readline())
    for case in range(1,T+1):
        ans = pancakes(str(f.readline().strip()))
        print "Case #%d: %s" % (case, ans)

