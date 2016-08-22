import sys
import itertools


def myrangebro(n):
    i = 2
    while i < n:
        yield i
        i += 1


def is_prime(number):
    for j in myrangebro(int(number**0.5 +1)):
        if number%j == 0:
            return False

    return True


def is_jamcoin(base_string):
    for base in range(2,11):
        if is_prime(int(base_string, base)):
            return False

    return True


def get_nt_divisor(num):
    for base in myrangebro(num):
        if (num % base) == 0:
            return base


with open(sys.argv[1], 'r') as f:

    fout = open(sys.argv[2], 'w')

    T = f.readline().strip('\n')

    for t in range(int(T)):
        line = f.readline().strip('\n')
        length, n = int(line.split(' ')[0]), int(line.split(' ')[1])

        fout.write("Case #" + str(t+1) + ':\n')

        args = ['1']
        for i in range(length-2):
            args.append('01')
        args.append('1')

        itr = itertools.product(*args)
        permuts = []
        count = n
        for s in itr:
            permuts.append(''.join(s))

        for base_string in permuts:

            if is_jamcoin(base_string):
                print base_string,
                fout.write(base_string + ' ')
                for base in range(2,11):
                    a = int(base_string,base)
                    fout.write(str(get_nt_divisor(a)) + ' ')
                fout.write('\n')
                print count
                count -= 1
            if count == 0:
                break

    fout.close
