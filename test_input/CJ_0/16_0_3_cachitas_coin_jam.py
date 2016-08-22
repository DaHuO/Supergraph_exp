from itertools import product
import logging
import math


log = logging.getLogger(__name__)


class Jamcoin:

    def __init__(self, s):
        self.s = s

        if not self.is_valid():
            raise InvalidJamcoin("Invalid jamcoin %s" % self.s)

    def __repr__(self):
        return self.s.__repr__()

    def __str__(self):
        """Returns the desired output str to represent this jamcoin.
        'jamcoin db2 db3 db4 db5 db6 db7 db8 db9 db10'
        where dbn is the divisor of base n.
        """
        s = "{jamcoin} {db2} {db3} {db4} {db5} {db6} {db7} {db8} {db9} {db10}"
        return s.format(
            jamcoin=self.s,
            db2=self.has_divisor(base=2),
            db3=self.has_divisor(base=3),
            db4=self.has_divisor(base=4),
            db5=self.has_divisor(base=5),
            db6=self.has_divisor(base=6),
            db7=self.has_divisor(base=7),
            db8=self.has_divisor(base=8),
            db9=self.has_divisor(base=9),
            db10=self.has_divisor(base=10)
        )

    def is_valid(self):
        log.info("Validating jamcoin %s", self.s)
        try:
            assert self.s.startswith('1')
            assert self.s.endswith('1')
            assert self.has_divisor(base=2), "No divisor for base 2"
            assert self.has_divisor(base=3), "No divisor for base 3"
            assert self.has_divisor(base=4), "No divisor for base 4"
            assert self.has_divisor(base=5), "No divisor for base 5"
            assert self.has_divisor(base=6), "No divisor for base 6"
            assert self.has_divisor(base=7), "No divisor for base 7"
            assert self.has_divisor(base=8), "No divisor for base 8"
            assert self.has_divisor(base=9), "No divisor for base 9"
            assert self.has_divisor(base=10), "No divisor for base 10"
        except AssertionError as e:
            log.debug("{} is not a valid jamcoin: {}".format(self.s, e))
            return False
        else:
            log.debug("{} is a valid jamcoin".format(self.s))
            return True

    def to_base(self, base):
        return sum(int(digit) * (base ** i)
                   for i, digit in enumerate(self.s[::-1]))

    def has_divisor(self, base):
        """
        A nontrivial divisor for a positive integer K is some positive
        integer other than 1 or K that evenly divides K.)
        For convenience, these divisors must be expressed in base 10.
        """
        log.debug("Checking if jamcoin has a divisor in base %d", base)
        log.debug("jamcoin in base %d: %d", base, self.to_base(base))
        number = self.to_base(base)

        # Divisor can't be 0, 1 or > number
        for divisor in range(2, int(math.sqrt(number)+1)):
            if divisor == number:
                return False
            if number % divisor == 0:
                return divisor


class InvalidJamcoin(ValueError):
    pass


def generate_jamcoins(N):
    all_strings = [''.join(t) for t in product('01', repeat=N)]
    log.debug('Generated {} strings with size {}'.format(len(all_strings), N))

    log.debug('Removing strings not starting or finishing in 1')
    strings = [s for s in all_strings if s.startswith('1') and s.endswith('1')]

    for s in strings:
        try:
            jamcoin = Jamcoin(s)
        except InvalidJamcoin as e:
            log.warning(e)
        else:
            log.debug("Value {}".format(
                      [jamcoin.to_base(b) for b in range(2, 11)]))
            log.debug("Divisors " + str(jamcoin))
            yield jamcoin


if __name__ == '__main__':

    logging.basicConfig(
        level='INFO',
        format='[%(levelname)-8s] %(name)s: %(message)s'
    )

    T = int(input())  # read a line with a single integer (input size)
    for i in range(1, T + 1):
        log.info(50 * '-' + ' CASE {:>d}'.format(i))
        N, J = [int(s) for s in input().split(" ")]
        log.info('Input: N={} and J={}'.format(N, J))
        print("Case #{}:".format(i))

        j = 0
        for jamcoin in generate_jamcoins(N):
            if j >= J:
                log.info("All jamcoins generated")
                break
            print(jamcoin)
            j += 1
        else:
            log.critical("Not enought jamcoins were generated!")
