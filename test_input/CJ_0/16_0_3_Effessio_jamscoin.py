# coding: utf-8


class JamcoinResolver:
    def __init__(self, length, num_coins):
        self.length = length
        self.num_coins = num_coins
        self.initial = int('1' + '0' * (self.length - 2) + '1', 2)
        self.max = int('1'*self.length, 2)

    def resolve(self):
        found = 0
        for candidate in self.generate_candidates():
            jamcoin, divisors = self.jamcoin_and_divisors(candidate)
            if jamcoin is not None:
                print '{} {}'.format(jamcoin, ' '.join([str(d) for d in divisors]))
                found += 1
                if found == self.num_coins:
                    return

    def jamcoin_and_divisors(self, candidate):
        divisors = []
        for base in range(2, 11):
            by_base = long(candidate, base)
            divisor = self.divisor(by_base)
            if divisor is None:
                return None, None
            divisors.append(divisor)
        return candidate, divisors

    @staticmethod
    def divisor(n):
        if n == 2:
            return 2
        if n == 3:
            return 2
        if n % 3 == 0:
            return 3
        r = int(n**0.5)
        f = 5
        while f <= r:
            if n % f == 0:
                return f
            if n % (f+2) == 0:
                return f + 2
            f += 6
        return None

    def generate_candidates(self):
        for num in range(self.initial, self.max + 1, 2):
            yield "{0:b}".format(num)

t = int(raw_input())
for i in xrange(1, t + 1):
    case_length, case_num_coins = [int(s) for s in raw_input().split(" ")]
    JamcoinResolver(case_length, case_num_coins).resolve()
