from os import getenv
from sys import argv, stdin

def debug(s, log):
    if getenv('DEBUG'):
        print s, log

def divisor(n):
    for i in xrange(2, int(n**0.5+1)):
        if n % i == 0:
            return i
    return 1

def check_coinjam(number):
    debug('check_coinjam: ', number)
    if not (number[0] == '1' and number[-1] == '1'):
        return False, []

    divisors = []
    for base in xrange(2, 10+1):
        n = int(str(number), base)
        div = divisor(n)
        debug('check_coinjam: check div => ', 'n: %d | div: %d' % (n, div))
        if div > 1:
            divisors.append(div)

    is_coinjam = len(divisors) == 9
    return is_coinjam, divisors


def get_answer(line):
    n, count = line.split(' ')
    n        = int(n)
    count    = int(count)
    zero     = int('1' + ((n-2) * '0') + '1', 2)
    m        = zero
    output   = {}
    while len(output) < count:
        cj_str = bin(m)[2:]
        is_coinjam, divisors = check_coinjam(cj_str)
        if is_coinjam and divisors not in output.values():
            output[cj_str] = divisors
        m += 1
    return output

if __name__ == '__main__':
    with (open(argv[1]) if len(argv) == 2 else stdin) as f:
        inputs = int(f.readline())
        for i in xrange(inputs):
            n = f.readline().strip()
            answer = get_answer(n)
            rt = '\n'
            for s in answer:
                rt += '%s %s \n' % (s, ' '.join(map(str, answer[s])))
            print "Case #%i: %s" % (i+1, rt),

