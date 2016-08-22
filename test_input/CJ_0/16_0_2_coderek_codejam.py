out = []


def permutation(s):
    ps = []

    def p(g, cur):
        if g == 0:
            ps.append(cur)
        else:
            p(g - 1, cur + '-')
            p(g - 1, cur + '+')
    p(s, '')
    return ps


def get_answer(cakes):
    table = {
        '+': 0,
        '-': 1,
    }

    def try_flip(s, pos):
        top = s[0:pos + 1]
        rev = top[::-1] + ''.join(['-' if c == '+' else '-' for c in s[pos:-1]])
        return table[rev[::-1][:-1]] + 2

    for s in range(2, len(cakes) + 1):
        perm = permutation(s)
        for p in perm:
            if p[-1] == '+':
                table[p] = table[p[:-1]]
            elif all(a == '-' for a in p):
                table[p] = 1
            else:
                i = len(p) - 1
                while p[i] == '-':
                    i -= 1
                table[p] = table[p[:i + 1]] + 2

    return table[cakes]


with open('input.in') as f:
    c = int(f.readline().strip())

    for n in range(c):
        i = f.readline().strip()
        ans = get_answer(i)
        out.append('Case #{n}: {ans}'.format(n=n+1, ans=ans))

with open('output', 'w') as f:
    f.write('\n'.join(out))


