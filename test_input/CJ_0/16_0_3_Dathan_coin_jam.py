import itertools
from jamcoins import gen_jamcoin_candidates
from primes import gen_primes

test_case = 'large'

# BASIC SETUP
import cStringIO

with open('{0}.in'.format(test_case)) as f:
    lines = f.readlines()
cases = int(lines.pop(0))

output = cStringIO.StringIO()
# END BASIC SETUP

coins = {}

jamcoins_with_divisors_in_all_bases = set()

for case in xrange(cases):
    line = lines[case].strip()
    coin_length, num_coins = [int(i) for i in line.split(' ')]

    counter = 0

    try:
        for d in gen_primes(2**32):
            print "Checking divisor {0}".format(d)
            for j in itertools.islice(gen_jamcoin_candidates(coin_length), 0, 1000000):
                for base in [2,3,4,5,6,7,8,9,10]:
                    n = int(j, base)
                    if n % d == 0:
                        coins[j] = coins.get(j, {})
                        coins[j][base] = coins[j].get(base, d)
                        if len(coins[j]) == 9:
                            jamcoins_with_divisors_in_all_bases.add(j)
                            if len(jamcoins_with_divisors_in_all_bases) == num_coins:
                                raise StandardError("Just breaking out of the loop")
    except StandardError:
        pass

    output_line = "Case #{0}:\n".format(case+1)
    for j in sorted(jamcoins_with_divisors_in_all_bases):
        divisors = coins[j]
        output_line += "{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}\n".format(
            j, divisors[2], divisors[3], divisors[4], divisors[5], divisors[6], divisors[7], divisors[8],
            divisors[9], divisors[10]
        )
    print output_line
    print >>output, output_line


### DEFAULT OUTPUT
with open('{0}.out'.format(test_case), 'w') as f:
    f.write(output.getvalue())
### DEFAULT OUTPUT
