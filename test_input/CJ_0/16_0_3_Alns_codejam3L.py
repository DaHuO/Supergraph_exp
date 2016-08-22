N, J = 32, 500


def find_factor(number, primes):
    i = 0
    p = primes[0]
    while p * p <= number:
        if number % p == 0:
            return p
        i += 1
        if i < len(primes):
            p = primes[i]
        else:
            break
    return 0


def primes_up_to(limit):
    is_prime = [False] * 2 + [True] * (limit - 1)
    for n in range(int(limit**0.5 + 1.5)):
        if is_prime[n]:
            for i in range(n * n, limit + 1, n):
                is_prime[i] = False
    for i in range(limit + 1):
        if is_prime[i]:
            yield i


def generate_coin(width, cnt):
    return '1' + bin(cnt)[2:].zfill(width - 2) + '1'


count = 0
printed = 0
divisor_candidates = list(primes_up_to(1000))
print('Case #1:')
while printed < J:
    coin = generate_coin(N, count)
    factor_list = []
    for base in range(2, 11):
        fct = find_factor(int(coin, base), divisor_candidates)
        if fct == 0:
            break
        factor_list.append(fct)
    if len(factor_list) == 9:
        printed += 1
        print(coin + ' ' + ' '.join(map(str, factor_list)))
    count += 1



