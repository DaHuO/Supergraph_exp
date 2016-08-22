import sys
import tempfile
import math


def main():
    input_file_path = sys.argv[1]
    fd, output_file_path = tempfile.mkstemp(prefix='q_c_output.txt')
    print "output file: " + output_file_path
    with open(input_file_path) as inf, open(output_file_path, 'w') as outf:
        lines = inf.readlines()
        num_of_tests = int(lines[0].strip())

        for i in range(1, num_of_tests + 1):
            N, J = lines[i].split()
            res = findJamcoins(int(N), int(J))
            outf.write("Case #{0}:\n".format(i))
            for r in res:
                outf.write(r + '\n')


def get_number_divider(num):
    i = 3
    mm = 13

    while i <= mm:
        if num % i == 0:
            return i
        i += 2
    return None


def tryJamcoins(jamcoin):
    tries = [int(jamcoin, 2), int(jamcoin, 3), int(jamcoin, 4), int(jamcoin, 5), int(jamcoin, 6),
             int(jamcoin, 7), int(jamcoin, 8), int(jamcoin, 9), int(jamcoin)]

    res = []

    for t in tries:
        div = get_number_divider(t)
        if div is None:
            return None
        res.append(str(div))
    return res


def findJamcoins(N, J):
    mm = 2**(N-2)
    n = 0
    res = []
    while J != 0:
        while n < mm:
            s = '1' + bin(n)[2:].zfill(N-2) + '1'

            r = tryJamcoins(s)

            if r is not None:
                res.append(s + ' ' + ' '.join(r))
                J -= 1
                if J == 0:
                    break
            n += 1
    return res


if __name__ == '__main__':
    main()
