from math import pow
import itertools
import struct

def main_loop(l, m):
    start = 1
    res_dict = {}

    while True:
        num = bin(start)[2:]
        fill_num = num.zfill(int(n))
        res_dict[fill_num] = []
        if len(fill_num) > l:
            res_dict.pop(fill_num)
            break
        if fill_num.startswith('0') or fill_num.endswith('0'):
            start += 1
            res_dict.pop(fill_num)
            continue
        for i in range(2,11):
            trans_num = trans(fill_num, i)
            d, is_prime = isPrime(trans_num)
            if is_prime:
                res_dict.pop(fill_num)
                break
            else:
                res_dict[fill_num].append(d)
        count = len(res_dict.keys())
        if count == m:
            break
        start += 1
    return res_dict

def trans(num, n):
    _sum = 0
    l = len(num) - 1
    for x in num:
        y = pow(n, l) * int(x)
        _sum += y
        l -= 1
    return _sum

def isPrime(n):
    if n <= 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return i, False
        i += 1
    return 0, True


if __name__ == "__main__":
    # import fileinput
    # f = fileinput.input("D:/B-large.in")
    #
    # T = int(f.readline())
    # for case in xrange(1, T+1):
    #     N = f.readline()
    #     res = flip(N)
    #
    #     print("Case #{0}: {1}".format(case, res))
    import fileinput
    f = fileinput.input("D:/C-small-attempt1.in")

    T = int(f.readline())

    n, m = [int(s) for s in f.readline().split(" ")]

    res = main_loop(int(n), int(m))
    print "Case #1:"
    for key, value in res.items()[:m]:
        out_string = str(key)
        for v in value:
            out_string += ' ' + str(v)
        print out_string
    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    # t = int(raw_input())  # read a line with a single integer
    # for i in xrange(1, t + 1):
    #     n = raw_input()  # read a list of integers, 2 in this case
    #     res = main_loop(int(n))
    #     print "Case #1:"
    #     for key, value in res.items()[:3]:
    #         out_string = str(key)
    #         for v in value:
    #             out_string += ' ' + str(v)
    #         print out_string
        # for base in range(2, 11):
        #     res = trans(n, base)
        #     is_prime = isPrime(res)
        #     print "Case #{}: {}".format(i, gen(5))

