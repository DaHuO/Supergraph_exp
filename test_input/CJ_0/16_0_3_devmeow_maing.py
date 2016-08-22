from math import sqrt
#from functools import lru_cache

IN = 'input.txt'
OUT = 'output.txt'


def to_bin(x, n):
    r = []
    while x:
        r.append(x % 2)
        x //= 2

    l = len(r)
    if l < n:
        r += [0] * (n - l)

    return r


def to_base_n(n, b):
    r = 0
    for i in range(len(b)):
        r += b[i] * n ** i

    return r


def get_div(x):
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return i

    return -1


def sol(line):
    n, u = map(int, line.split())
    n -= 2
    res = []
    k = 0
    for i in range(2 ** n):
        divs = []
        fail = False
        b = [1] + to_bin(i, n) + [1]
        for j in range(2, 11):
            x = to_base_n(j, b)
            d = get_div(x)
            if d == -1:
                fail = True
                break
            divs.append(d)
        if fail:
            continue
        res.append('{} {}'.format(
            ''.join(list(map(str, [1] + to_bin(i, n)[::-1] + [1]))),
            ' '.join(list(map(str, divs)))
        ))
        k += 1
        if k == u:
            break

    return '\n' + '\n'.join(res)


def main():
    with open(IN, 'r') as f, open(OUT, 'w') as g:
        t = int(f.readline())
        for i in range(t):
            g.write('Case #{}: '.format(i + 1))
            g.write(sol(f.readline().strip()))
            g.write('\n')


if __name__ == '__main__':
    main()
