# Coin Jam

def get_primes(max_num):
    primes = []
    is_prime = [True] * (max_num + 1)
    for i in range(2, int(max_num ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i, max_num / i + 1):
                is_prime[i * j] = False
    for i in range(2, max_num + 1):
        if is_prime[i]:
            primes.append(i)
    return primes

def min_divisor(num, primes):
    for divisor in primes:
        if num % divisor == 0:
            return divisor
    return num # likely to be a prime

def get_divisors(jamcoin, primes):
    divisors = []
    for base in range(2, 11):
        num = int(jamcoin, base)
        divisor = min_divisor(num, primes)
        if divisor == num:
            return None
        divisors.append(divisor)
    return divisors

def main():
    f_in = open('C-large.in.txt', 'r')
    f_out = open('C-large.out.txt', 'w')

    n_tests = int(f_in.readline())

    primes = get_primes(100000)

    for i in range(n_tests):
        f_out.write('Case #{}:\n'.format(i + 1))

        params = f_in.readline().split(" ")
        N = int(params[0])
        J = int(params[1])

        num = int('1' + '0' * (N - 2) + '1', 2)
        while J > 0:
            jamcoin = format(num, 'b')
            divisors = get_divisors(jamcoin, primes)

            if divisors != None:
                J -= 1
                f_out.write(jamcoin + ' ' + ' '.join(map(str, divisors)) + '\n')
            num += 2

    f_in.close()
    f_out.close()

if __name__ == "__main__":
    main()
