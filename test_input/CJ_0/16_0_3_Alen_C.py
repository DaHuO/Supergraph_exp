#!/usr/bin/env python
# encoding: utf-8

def parseCase(line):
    return line.split(" ")


primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
31, 37, 41, 43, 47, 53, 59, 61, 67,
71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
173, 179, 181, 191, 193, 197, 199, 211, 223, 227,
229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
281, 283, 293, 307, 311, 313, 317, 331, 337, 347,
349, 353, 359, 367, 373, 379, 383, 389, 397, 401,
409, 419, 421, 431, 433, 439, 443, 449, 457, 461,
463, 467, 479, 487, 491, 499, 503, 509, 521, 523,
541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
601, 607, 613, 617, 619, 631, 641, 643, 647, 653,
659, 661, 673, 677, 683, 691, 701, 709, 719, 727,
733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
809, 811, 821, 823, 827, 829, 839, 853, 857, 859,
863, 877, 881, 883, 887, 907, 911, 919, 929, 937,
941, 947, 953, 967, 971, 977, 983, 991, 997)


def min_nontrivial_divisor(n):
    for p in primes:
        if n % p == 0:
            return p
    return 0


def is_jam_coin(n_str):
    result = ""
    for base in range(2, 11):
        n = int(n_str, base)
        d = min_nontrivial_divisor(n)
        if d > 0:
            # result = result + " " + str(n) + ": " + str(d) + ", "
            result = result + " " + str(d)
        else:
            return None
    return result


def solve(caseLine):
    n, j = parseCase(caseLine)
    n = int(n)
    j = int(j)
    c = 0
    result = ""
    s = int(format(1 << (n - 1), 'b'), 2)
    e = int(format(1 << n, 'b'), 2)
    for i in range(s, e):
        i_str = format(i, 'b')
        if not i_str.endswith("1"):
            continue
        r = is_jam_coin(i_str)
        if r is not None:
            c += 1
            result += i_str + r + "\n"
            if c >= j:
                break
    return result

def run(inputFile, outputFile):
    fp = open(inputFile, 'r')
    fw = open(outputFile, 'w')
    caseIndex = 0
    count = -1
    for line in fp:
        if (caseIndex == 0):
            count = int(line)
            caseIndex += 1
        else:
            fw.write("Case #%d: \n%s\n" % (caseIndex, solve(line)))
            caseIndex += 1
            count -= 1
        if (count == 0):
            break
    fp.close()
    fw.close()


if __name__ == "__main__":
    run("in", "out")