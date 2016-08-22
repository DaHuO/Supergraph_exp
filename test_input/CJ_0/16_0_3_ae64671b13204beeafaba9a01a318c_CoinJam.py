test_input = \
"""1
16 50"""
test_output = \
"""Case #1:
100011 5 13 147 31 43 1121 73 77 629
111111 21 26 105 1302 217 1032 513 13286 10101
111001 3 88 5 1938 7 208 3 20 11"""
test = True
line_number = 0

"""
A jamcoin is a string of N >= 2 digits with the following properties:

Every digit is either 0 or 1.
The first digit is 1 and the last digit is 1.
If you interpret the string in any base between 2 and 10, inclusive, the resulting number is not prime.
"""


def get_input():
    global line_number
    if not test:
        return raw_input("")
    else:
        output = test_input.split("\n")[line_number]
        line_number += 1
        return output

# from https://stackoverflow.com/questions/1801391/what-is-the-best-algorithm-for-checking-if-a-number-is-prime
def isPrime(n):
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


if __name__ == "__main__":
    cases = int(get_input())
    for case in range(cases):
        # we only have one case for this one
        length, examples_count = get_input().split()
        length = int(length)
        examples_count = int(examples_count)
        first_number = int("1" + "0" * (length - 2) + "1", 2)
        last_number = int("1" * length, 2)

        #print first_number, last_number
        current_number = first_number
        examples = []
        first = True
        while len(examples) < examples_count:
            if first:
                first = False
            else:
                current_number += 2
                #if len("{0:b}".format(current_number)) > length:
                if current_number > last_number:
                    raise Exception("Unable to find enough valid numbers, just went past last number!")
            if isPrime(current_number):
                continue
            binary_string = "{0:b}".format(current_number)
            valid = True
            for i in range(2, 11):
                if isPrime(int(binary_string, i)):
                    valid = False
                    break
            if valid:
                output = "{} ".format(binary_string)
                for i in range(2, 11):
                    current_base = int(binary_string, i)
                    factor = None
                    j = 2
                    while j < current_base - 1:
                        if current_base % j == 0:
                            factor = j
                            break
                        j += 1
                    if factor:
                        output += "{} ".format(factor)
                    else:
                        raise Exception("Seriously?")
                examples.append(output.strip())
        print "Case #{}:".format(case + 1)
        for line in examples:
            print line
