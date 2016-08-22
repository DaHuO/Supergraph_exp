# https://code.google.com/codejam/contest/6254486/dashboard#s=p1
import fileinput


def mapper(st):
    if st == '-':
        return -1
    elif st == '+':
        return 1


def transform(st):
    return [mapper(c) for c in list(st)]


def turn(l, n):
    return [i * -1 for i in l[0:n]] + l[n:len(l)]


def simulate(st, turns):
    l = transform(st)
    print(l)
    for t in turns:
        l = turn(l, t)
        print(l)


def solve(st):
    result = 0
    if st[-1] == '-':
        result += 1
    prev = st[0]
    if len(st) > 1:
        for c in st[1:]:
            if c != prev:
                result += 1
            prev = c
    return result


if __name__ == '__main__':
    f = fileinput.input()
    T = int(f.readline())
    for case in range(1,T+1):
        s = f.readline()
        print("Case #{0}: {1}".format(case, solve(s.strip())))
