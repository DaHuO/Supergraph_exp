import sys
import string
import math

def int2base(integer, base):
    if not integer: return '0'
    sign = 1 if integer > 0 else -1
    alphanum = string.digits + string.ascii_lowercase
    nums = alphanum[:base]
    res = ''
    integer *= sign
    while integer:
            integer, mod = divmod(integer, base)
            res += nums[mod]
    return ('' if sign == 1 else '-') + res[::-1]

def is_prime(n):
    n = abs(int(n))
    if n < 2:
        return 1

    if n == 2: 
        return -1

    for x in xrange(3, int(n**0.5) + 1):
        if n % x == 0:
            return x

    return -1

def process(length, res_num):
    start_num = 2 ** (length - 1) + 1
    end_num = 2 ** length
    res = []
    for num in xrange(start_num, end_num, 2):
        if len(res) == res_num:
            return '\n'.join(res)
        is_valid = True
        divisors = []
        num_in_base2 = int2base(num, 2)
        for base in range(2, 11):
            num_in_base = int(num_in_base2, base)
            divisor = is_prime(num_in_base)
            if divisor == -1:
                is_valid = False
                break;
            divisors.append(str(divisor))
        if is_valid:
            res.append(int2base(num, 2) + ' ' + ' '.join(divisors))
    
if __name__ == '__main__':
    res = ''
    i = 0
    with open('input', 'r') as file:
        first = True
        for line in file:
            if first:
                first = False
                continue;
            i = i + 1
            splitted = line.split(' ')
            res = res + ("Case #%s: \n%s" % (i, process(int(splitted[0]), int(splitted[1]))))

    with open('output', 'w+') as file:
        print res
        file.write(res)