import sys


def check_bit(i, k):
    return (i & 1 << k) != 0


def is_prime(n):
    rst = []
    '''check if integer n is a prime'''

    # make sure n is a positive integer
    n = abs(int(n))

    # 2 is the only even prime number
    if n == 2:
        return 2

    # range starts with 3 and only needs to go up
    # the square root of n for all odd numbers
    for x in range(2, 50):
        if n % x == 0:
            return x

    return None


def check_num(orignal):
    rst = []
    for i in range(2, 11):
        tmp = int(original, i)
        divisor = is_prime(tmp)
        if divisor is None:
            return
        rst.append(divisor)
    print(original + ' ' + ' '.join(str(x) for x in rst))
    return True

I = iter(sys.stdin)

test = next(I)
N = int(next(I))
J = int(next(I))
count = 0
print("Case #1:")
for i in range(2 ** (N - 1) + 1, 2 ** N):
    if check_bit(i, 0) == True and check_bit(i, N - 1) == True:
        original = bin(i)[2:]
        if check_num(original):
            count += 1
            if count == J:
                break
