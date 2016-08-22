import datetime
import math
import time

from utils import primes

__author__ = 'eegee'

filename = "C-large"

input_data = open("../data/" + filename + ".in")
output_data = open("../data/" + filename + ".out", "w")
time.perf_counter()

# read inputs #
input_data.readline()
output_line = "Case #1:"
print(output_line)
output_data.write(output_line + "\n")

length, count = list(map(int, input_data.readline().split()))
# read inputs #

answer = ""
# solution #
i = 0
while count:
    jamcoin = ("1{:0>" + str(length - 2) + "}1").format(bin(i)[2:])
    divisors = []

    for base in range(2, 11):
        computed_number = int(jamcoin, base)
        no_divisor = True
        if primes.is_prime(computed_number):
            break

        prime = 1
        while prime < 999999:  # math.sqrt(computed_number)
            prime = primes.next_prime(prime)
            if (computed_number % prime) == 0:
                divisors.append(prime)
                break

    if len(divisors) == 9:
        print(jamcoin, " ".join(map(str, divisors)))
        output_data.write(jamcoin + " " + " ".join(map(str, divisors)) + "\n")
        count -= 1

    i += 1
# solution #

print()
print("total_time:", datetime.timedelta(seconds=time.perf_counter()))
input_data.close()
output_data.close()