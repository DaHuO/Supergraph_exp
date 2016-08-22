
ps = []
def build_ps():
    n = 1000
    vis = [False for i in xrange(n)]

    for i in xrange(2, n):
        if not vis[i]:
            ps.append(i)
            for j in xrange(i*i, n, i):
                vis[j] = True


def solve(s):
    facs = []
    for j in xrange(2, 10+1):
        val = int(s, j)

        for p in ps:
            if val % p == 0:
                #print s, j, val, p
                facs.append(p)
                break
        else:
            return None

    return facs


def main():
    build_ps()

    T = int(raw_input())
    for zi in xrange(T):
        N, J = map(int, raw_input().split())

        M = 1 << (N - 2)
        cnt = 0
        print 'Case #%d:' % (zi + 1)

        for i in xrange(M):
            val = 1 << (N - 1) | (i << 1) | 1
            s = bin(val)[2:]

            facs = solve(s)
            if facs:
                print s, ' '.join(map(str, facs))
                cnt += 1

            if cnt >= J:
                break


main()
