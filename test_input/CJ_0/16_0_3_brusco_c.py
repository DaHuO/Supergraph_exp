import math


def trial_division(n):
    candidate = 2
    # no need to find a divisor by all means, just skip it if not found soon
    max_candidate = min(math.sqrt(n), 1000)
    while candidate < max_candidate:
        if n % candidate == 0:
            return candidate
        # next candidate
        if candidate == 2:
            candidate = 3
        else:
            # skipping even candidates
            candidate += 2
    return None

binary = lambda number: bin(number)[2:]

if __name__ == "__main__":
    raw_input()
    length, jamcoins_count = tuple(int(value) for value in raw_input().split())

    print "Case #1:"

    found_jamcoins = 0
    for i in xrange(0, pow(2, length - 2)):
        coin = binary(i)
        coin = "1" + ("0" * (length - 2 - len(coin))) + coin + "1"
        divisors = []
        for base in xrange(2, 11):
            interpretation = int(coin, base)
            divisor = trial_division(interpretation)
            if divisor is None:
                break
            else:
                divisors.append(divisor)

        if len(divisors) == 9:
            print coin, " ".join([str(divisor) for divisor in divisors])
            found_jamcoins += 1

        if found_jamcoins == jamcoins_count:
            break
