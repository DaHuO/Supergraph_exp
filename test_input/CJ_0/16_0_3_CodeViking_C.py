import os, sys, time

sys.setrecursionlimit(500000)


class ReadWrite:
    def __init__(self, file_name=None, verbose=True):
        self.verbose = verbose
        if file_name is None:
            self.in_file = sys.stdin
            self.out_file = sys.stdout
        else:
            self.in_file = open(file_name)
            self.out_file = open(os.path.splitext(file_name)[0] + '.out', 'w')
        self.case_idx = 1

    def msg(self, output, end='\n'):
        sys.stderr.write(str(output) + end)

    def read_line(self, *types, all=None):
        words = self.in_file.readline().strip().split()
        if all is not None:
            return [all(w) for w in words]
        if len(types) == 0:
            return words
        assert (len(words) == len(types))
        if len(types) == 1:
            return types[0](words[0])
        return [t(w) for t, w in zip(types, words)]

    def write_case(self, output, true="YES", false="NO", join='\n'):
        pfx = "Case #%d:" % self.case_idx
        self.case_idx += 1
        if isinstance(output, list):
            text = join.join([pfx] + output)
        elif isinstance(output, bool):
            text = pfx + ' ' + (true if output else false)
        else:
            text = pfx + ' ' + str(output)
        self.out_file.write(text + '\n')
        if self.verbose:
            self.msg(text)
        else:
            self.msg(pfx)


def padded_bin(x, width):
    xb = bin(x)[2:]
    n = len(xb)
    if n < width:
        return '0' * (width - n) + xb
    assert (n == width)
    return xb


QUIT_TRYING = 100


def find_nontrivial_divisor(n):
    if n <= 3:
        return None
    if n % 2 == 0:
        return 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return d
        d += 2
        if d > QUIT_TRYING:
            break
    return None


def find_jam_coin_divisors(jc):
    result = []
    for base in range(2, 11):
        n = int(jc, base)
        d = find_nontrivial_divisor(n)
        if d is None: return None
        result.append(d)
    return result


def solve(N, J):
    s = time.time()
    inner_bits = N - 2
    valid_coins = []
    for inside in range(2 ** inner_bits):
        jc = '1' + padded_bin(inside, inner_bits) + '1'
        divs = find_jam_coin_divisors(jc)
        if divs is None: continue
        valid_coins.append(' '.join([str(x) for x in ([jc] + divs)]))
        if len(valid_coins) >= J:
            break
    if len(valid_coins) < J:
        return None
    return valid_coins


if __name__ == '__main__':

    input_name = sys.argv[1] if len(sys.argv) > 1 else 'C-tiny-practice.in'
    rw = ReadWrite(input_name)
    T = rw.read_line(int)
    for t in range(T):
        N, J = rw.read_line(int, int)
        rw.write_case(solve(N, J))
