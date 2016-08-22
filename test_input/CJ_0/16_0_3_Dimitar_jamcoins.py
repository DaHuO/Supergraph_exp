from sys import stdin, stdout, stderr


def store(n, j):
    pass


def load(n, j):
    pass


def nums(fd, t):
    l = fd.readline()
    return [t(n) for n in l.split(" ")]


def solve(n, j):
    pass

def maybe_composite(n):
    for i in range(2, min(n - 1, 100)):
        if n % i == 0:
            return True, i
    return False, 1


def values(i, bases=range(2, 11)):
    for b in bases:
        yield int(i, b)

def jamcoin(i):
    res = [i]
    for n in values(i):
        r = maybe_composite(n)
        if r[0]:
            res.append(r[1])
        else:
            return []
    return res


def jamcoins(n, j):
    candidate = '1' * n
    c = 0
    while c < j:
        jam = jamcoin(candidate)
        if jam:
            c += 1
            yield jam
        candidate = bin((int(candidate, 2) - 2))[2:]


if __name__ == "__main__":
    cases = int(stdin.readline())
    for c in range(1, cases + 1):
        N, J = nums(stdin, int)
        ans = jamcoins(N, J)
        stdout.write("Case #{0}:\n".format(c))
        for l in ans:
            stdout.write(" ".join(str(i) for i in l))
            stdout.write("\n")
