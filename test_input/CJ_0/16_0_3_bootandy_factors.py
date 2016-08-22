import math

# c = 1234567890123456
#
# print(c / 12345)
#
# n = 1234567890123456
# for i in range(1, int(math.sqrt(c))):
#     if n % i == 0:
#         print i


# for i in range(2, 10):
#     print (i ** 4)
#
# ans = 1
#
# for i in [2,3,5,7,11,13,17]:
#     ans = ans * i
#
# a = ans
# while True:
#     a = a + ans
#     print a
N = 16
J = 50

def primes_sieve(limit):
    limitn = limit+1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*2, limitn, i):
            not_prime.add(f)

        primes.append(i)

    return primes

primes = primes_sieve(12345)

# print('got primes')

def recur(s, level):
    if level == 0:
        return [s + '01', s + '11']
    return recur(s + '0', level-1) + recur(s+'1', level-1)

bin_strings = recur('1', N - 3)

# print('build bin strings')
# print(bin_strings)

num_found = 0
print('Case #1:')

for a_bin in bin_strings:
    nums = []
    for i in range(2, 11):
        to_test = int(a_bin, i)
        for p in primes:
            if to_test % p == 0:
                nums.append(p)
                break

    if len(nums) == 9:
        print('%s %s' %(a_bin, ' '.join(map(str, nums))))
        num_found += 1
        if num_found >= J:
            break

