__author__ = 'apoorvab'
#Isn't it Pythonic... Don't you think?
import multiprocessing

def get_parsed_line():
    return list(map(int, input().split()))


def get_case():
    line = get_parsed_line()
    length = line[0]
    req_coins = line[1]

    return (length, req_coins)


def get_divisors(number):

    divisors = []

    for base in range(2, 11):
        # print(int(bin(coin)[2:], base), get_divisor(int(bin(coin)[2:], base)))
        try:
            divisors.append(get_divisor(int(bin(number)[2:], base)))
        except Exception:
            return None
            raise Exception()

    return number, divisors

# Adapted from https://stackoverflow.com/questions/15285534/isprime-function-for-python-language
def get_divisor(number):

    if number == 2 or number == 3: raise Exception()
    if number < 2 or number % 2 == 0: return 2
    if number < 9: return Exception()
    if number % 3 == 0: return 3

    r = int(number ** 0.5)
    f = 5

    while f <= r:
        if number % f == 0: return f
        if number % (f + 2) == 0: return f + 2
        f += 6

    raise Exception()


if __name__ == '__main__':
    num_cases = get_parsed_line()[0]
    num_threads = multiprocessing.cpu_count()

    for case_num in range(0, num_cases):

        length, req_coins = get_case()
        test_coin = int('1' + (length - 2) * '0' + '1', 2)
        num_coins = 0
        jam_coins = []

        print('Case #%d:' % (case_num + 1))

        while len(jam_coins) < req_coins:
            jobs = list(range(test_coin, test_coin+20*req_coins, 2))
            test_coin += req_coins

            with multiprocessing.Pool(num_threads) as pool:
                results = pool.map(get_divisors, jobs)

            jam_coins.extend([(result[0], result[1]) for result in results if result is not None])

        jam_coins = jam_coins[0:req_coins]

        for jam_coin in jam_coins:
            number, divisors = jam_coin
            print(bin(number)[2:], ' '.join(map(str, divisors)))

        # Single thread
        # while num_coins != req_coins:
        #     try:
        #         divisors = get_divisors(test_coin)
        #         num_coins += 1
        #         print(bin(test_coin)[2:], ' '.join(map(str, divisors)))
        #     except Exception:
        #         ...
        #
        #     test_coin += 2
