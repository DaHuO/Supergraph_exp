__author__ = 'chiselko6'
N = 100000
tests, n, J = map(int, raw_input().split())


def bin_gen():
    val = 1 << (n - 1)
    val += 1
    while True:
        yield val
        val += 2


def check(val, base, delim):
    a = 0
    for i in xrange(len(val)):
        a += int(val[len(val) - i - 1]) * base**i
    return a % delim == 0

primes = []
_primes = [False] * (N + 5)


def init_primes():
    for i in xrange(2, N):
        if not _primes[i]:
            primes.append(i)
            j = i
            while j <= N:
                _primes[j] = True
                j += i


init_primes()

with open('output.txt', 'w') as fout:
    fout.write('Case #1:\n')
    for bin_val in bin_gen():
        if not J:
            break
        binary = bin(bin_val)[2:]
        delims = []
        for i in xrange(9):
            number = int(binary, i + 2)
            if number in primes:
                break
            for x in primes:
                if number % x == 0:
                    delims.append(x)
                    break
        if len(delims) == 9:
            fout.write(binary)
            fout.write(' ')
            # print binary,
            for idx, i in enumerate(delims):
                if not check(binary, idx + 2, i):
                    print 'NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO'
                fout.write(str(i))
                fout.write(' ')
                # print i,
            # print
            fout.write('\n')
            J -= 1
