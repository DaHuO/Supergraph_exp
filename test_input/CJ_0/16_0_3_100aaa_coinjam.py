import sys
from math import sqrt
import random

def main(argv=sys.argv):
    output = open("C-small-attempt0.out", "w")
    input = open("C-small-attempt0.in", "r")
    T = int(input.readline().rstrip())
    second_line = input.readline().rstrip()
    N = int(second_line.split(' ')[0])
    J = int(second_line.split(' ')[1])

    output.write("Case #1:\n")

    completed = 0

    for i in range(0, pow(2, N-2)):
        middle = bin(i).split('0b')[1]
        padding = ''
        for j in range(len(middle),N-2):
            padding += '0'
        candidate = '1' + padding + middle + '1'
        bases = generate_base(candidate)

        if has_prime(bases) == True:
            continue

        interpretations = []
        for base in bases:
            interpretation = get_interpretation(base)
            if interpretation > 0:
                interpretations.append(str(interpretation))

        if len(interpretations) < 9:
            continue

        processed = candidate + " " + " ".join(interpretations)
        output.write(processed + "\n")
        completed += 1

        if completed == J:
            break

    output.close()
    input.close()

def generate_base(jamcoin):
    bases = []
    for base in range(2, 11):
        sum = 0
        digit = 0
        for i in reversed(jamcoin):
            sum += int(i) * int(pow(base, digit))
            digit += 1
        bases.append(sum)
    return bases

def has_prime(bases):
    for base in bases:
        if is_prime(base) == True:
            return True
    return False

"""
def is_prime(n):
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
    while True:
        if i * i <= n:
            break
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True
"""

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def get_interpretation(base):
    if base % 2 == 0 and base != 2:
        return 2
    if base % 3 == 0 and base != 3:
        return 3
    if base % 5 == 0 and base != 5:
        return 5
    if base % 7 == 0 and base !=7 :
        return 7
    if base % 11 == 0 and base != 11:
        return 11
    n = 12
    while True:
        if n > sqrt(base):
            break
        if base % n == 0:
            return n
        n += 1
    return 0

if __name__ == "__main__":
    main()