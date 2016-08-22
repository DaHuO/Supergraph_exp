# out = []
# 
# 
# with open('input.in') as f:
#     c = int(f.readline().strip())
# 
#     for n in range(c):
#         i = f.readline().strip()
#         ans = table(i)
#         out.append('Case #{n}: {ans}'.format(n=n+1, ans=ans))
# 
# with open('output', 'w') as f:
#     f.write('\n'.join(out))
# 
# 


def permutate(n):
    res = []

    def p(n, cur):
        if n == 0:
            res.append(cur)
            return
        p(n - 1, cur + '0')
        p(n - 1, cur + '1')
    p(n, '')

    return res


def check_base(c, b):
    dec = 0
    d = 0
    for i in range(len(c) - 1, -1, -1):
        dec += pow(b, d) * int(c[i])
        d += 1

    k = 2
    while k * k < dec:
        if dec % k == 0:
            return str(dec / k)
        k += 1
    return None


def check(c):
    if c[0] != '1' or c[-1] != '1':
        return None
    factors = []
    # base
    for b in range(2, 11):
        factor = check_base(c, b)
        if factor:
            factors.append(factor)
        else:
            return None
    return factors


def solve():
    n = 16
    j = 50

    results = []

    for c in permutate(n):
        res = check(c)
        if res:
            results.append([c] + res)
        if len(results) == j:
            return results


with open('output', 'w') as f:
    results = solve()
    f.write('\n'.join([
        'Case #1:',
    ] + [' '.join(r) for r in results]))
