from __future__ import division

# N, J = 16, 50
N, J = 32, 500


def gen_bin(k=0):
    n = N - 2
    while True:
        b = bin(k)[2:]
        if len(b) > n:
            yield None
        m = '0' * (n - len(b)) + b
        s = '1' + m + '1'
        k += 1
        yield s

bins = gen_bin()


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True


test = ['0011', 5, 13, 147, 31, 43, 1121, 73, 77, 629]
case_list = []


def first_factor(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    return -1


def get_factors(bases):
    for k in bases:
        if is_prime(k):
            return None
    factors = [first_factor(n) for n in bases]
    if -1 in factors:
        return None
    return factors


def make_cases():
    b = bins.next()
    while b is not None and len(case_list) < J:
        bases = [int(b, k) for k in range(2, 11)]
        f = get_factors(bases)
        if f is not None:
            case_list.append([b] + f)
            # print case_list[-1]
        b = bins.next()


def write(fname, case_list):
    with open(fname, 'wb') as fid:
        fid.write('Case #1:\n')
        for case in case_list:
            r = ' '.join(str(x) for x in case[1:])
            s = '{} {}\n'.format(case[0], r)
            # s = s.format(case[0])
            fid.write(s)


def main():
    make_cases()
    outfile = 'C-large_small.txt'
    write(outfile, case_list)

if __name__ == '__main__':
    main()
