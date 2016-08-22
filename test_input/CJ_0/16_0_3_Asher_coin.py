import functools
import signal
from contextlib import contextmanager


time_out = 1

class TimeoutException(Exception):
    pass


@contextmanager
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException("Timed out!")
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)


def base_n(num, b, numerals="0123456789"):
    return ((num == 0) and numerals[0]) or (base_n(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])


@functools.lru_cache(maxsize=None)
def is_prime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


def generate_prime_coins(length, total_coins=-1):
    temp_length = length-2
    max_num = 2**temp_length

    count = 0

    for i in range(max_num):
        if count == total_coins:
            break

        s = base_n(i, 2)
        if len(s) < temp_length:
            s = "0" * (temp_length - len(s)) + s

        s = "1{}1".format(s)

        prime = False

        for i in range(2, 11):
                try:
                    with time_limit(time_out):
                        if is_prime(int(s, i)):
                            prime = True
                            break
                except TimeoutException:
                    pass

        if not prime:
            count += 1
            yield s


@functools.lru_cache(maxsize=None)
def find_coin_factor(coin):
    if coin % 2 == 0:
        return 2
    if coin % 3 == 0:
        return 3

    for i in range(5, int(coin ** 0.5) + 1, 2):
        if coin % i == 0:
            return i


file_out = "big.out"


def write_to_file(string):
    with open(file_out, "a") as f:
        f.write("{}\n".format(string))

length = 32

total_coins = 500

written = 0

write_to_file("Case #1:")
for coin in generate_prime_coins(length):
    try:
        with time_limit(time_out):
            results = [coin,
                       str(find_coin_factor(int(coin, 2))),
                       str(find_coin_factor(int(coin, 3))),
                       str(find_coin_factor(int(coin, 4))),
                       str(find_coin_factor(int(coin, 5))),
                       str(find_coin_factor(int(coin, 6))),
                       str(find_coin_factor(int(coin, 7))),
                       str(find_coin_factor(int(coin, 8))),
                       str(find_coin_factor(int(coin, 9))),
                       str(find_coin_factor(int(coin, 10)))]
            write_to_file(" ".join(results))

            written += 1

            print(written)
            if written == 500:
                break
    except TimeoutException:
        pass

