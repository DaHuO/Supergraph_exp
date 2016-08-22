import sys

def sieve(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    i=2
    while (i * i <= n):
        if (sieve[i]):
          k=i * i
          while (k <= n):
              sieve[k] = False
              k += i
        i += 1
    return sieve


def get_divisor(n):
    i = 2
    while (i * i <= n):
        if (n % i == 0):
            return i
        i += 1
    return None


def all_jam_coins(N):
    ret = []
    for i in xrange(0, 2**(N-2)-1):
        bin_str = bin(i)[2:]
        bin_str = '0'*(N-2-len(bin_str)) + bin_str
        bin_str = '1' + bin_str + '1'
        res, div = test_jam(bin_str)
        if res:
            ret.append((bin_str, div))
        if len(ret) == 50:
            break
    return ret

def test_jam(bin_str):
    ret = [get_divisor(int(bin_str, i)) for i in xrange(2, 11)]
    return (all(ret), ret)


if __name__ == "__main__":
    N = 16
    res = all_jam_coins(N)
    output_file = open("%s.%s" % ("jam_coin_small", "out"), "w")
    output_file.write("Case #%s:\n" % (1,))
    for i in xrange(len(res)):
        output_file.write(
            "%s %s\n" % (res[i][0], " ".join(map(str, res[i][1]))))
    output_file.close()
    print "Done!"
