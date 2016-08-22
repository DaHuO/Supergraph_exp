import itertools

import math


def main(N, J):
    numbers = possible_ns(N)
    num_tuples = []
    for num in numbers:
        if len(num_tuples) == J:
            break
        #http://stackoverflow.com/questions/2267362/convert-integer-to-a-string-in-a-given-numeric-base-in-python
        divisors = []
        fr = 2
        to = 11
        bases_count = to - fr
        for base in range(fr, to):
            base_num = int(str(num), base)
            if is_prime(base_num):
                break
            divisors.append(get_next_divisor(base_num, divisors))
        if len(divisors) == bases_count:
            num_tuples.append((num, divisors))
    return num_tuples


def possible_ns(N):
    numbers = []
    for i in itertools.product([0, 1], repeat=N):
        if i[0] == 1 and i[-1] == 1:
            numbers.append(int(''.join(map(str, i))))
    return numbers


#http://stackoverflow.com/questions/171765/what-is-the-best-way-to-get-all-the-divisors-of-a-number
def divisor_generator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


def get_next_divisor(n, prev_divisors):
    for d in divisor_generator(n):
        if d not in prev_divisors and d != 1 and d != n:
            return d
    return None


#https://en.wikipedia.org/wiki/Primality_test
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    file_name = "C-small-attempt0.in"
    #file_name = "input"
    with open(file_name, 'r') as f:
        _ = int(f.readline())
        N, J = list(map(int, f.readline().split(' ')))
    output_tuples = main(N, J)
    print "N=%s,J=%s: len(output_tuples)=%s" % (N, J, len(output_tuples))
    output = ["Case #1:"]
    for o in output_tuples:
        output.append(str(o[0]) + " " + " ".join(map(str, o[1])))
    output = "\n".join(output)
    print output
    fo = open(file_name + "_output", "w")
    fo.write(output)