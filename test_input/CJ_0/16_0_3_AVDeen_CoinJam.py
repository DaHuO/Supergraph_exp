import sys

__author__ = 'vandeen'


# 1) Walk through possible Coinjam combination of given length
#       Coinjams are:
#           Every digit is either 0 or 1
#           First and last digit is 1
# Look for coinjams from 10...01 to 11...11 of length n
# yield any successful coinjam strings, along with list of non-trivial divisors for each base
def find_coinjams(length):
    curr = 0
    n = length - 2
    while curr < (2 ** n):
        divs = []
        coinjam = "1" + format(curr, '0%db' % n) + "1"
        divs = find_coinjam_divisors(coinjam)
        if divs == []:
            curr += 1
            continue
        else:
            curr += 1
            yield coinjam, divs


# 2) Interpret coin jam as each base from 2-10
# interprets string as a number from base 2-10
# if each number is not prime, return a list of non-trivial divisors for each base
# else return empty list
def find_coinjam_divisors(jam):
    bases = [base for base in range(2, 11)]
    divisors = []
    for base in bases:
        divisor = find_divisor(number_as_base(int(jam), base))
        if divisor == 0:
            return []
        else:
            divisors.append(divisor)
    return divisors


def number_as_base(num, base):
    value = 0
    place = 0
    while num:
        value += (int(num % 10) * (int(base) ** place))
        num //= 10
        place += 1
    return value


# 3) Find a non-trivial divisor
# Attempts to find a non-trivial divisor for given number
# else returns 0
def find_divisor(num):
    i = 2
    while i * i <= num:
        if num % i != 0:
            i += 1
            # Don't waste time with the ones that take forever, more fish in the sea
            if i > 1000:
                break
        else:
            return i
    return 0


if __name__ == "__main__":
    file = sys.argv[1]

    with open(file) as fh:
        fh.readline()  # Strip first line, don't need it (Always 1 case)
        output = open("test.out", "w")

        # number of Coinjams of length length
        length, number = tuple(int(n) for n in fh.readline().split())
        found = 0
        output.write("Case #1:\n")

        # find coin jams
        # break when number are found
        for cj in find_coinjams(length):
            found += 1
            cj, divs = cj
            print(cj, " ".join([str(s) for s in divs]))  # For debugging
            output.write(cj + " " + " ".join([str(s) for s in divs]) + "\n")
            if found >= number:
                break