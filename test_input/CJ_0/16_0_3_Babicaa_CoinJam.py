import sys
import math

__author__ = 'andrej.babic@ringlspil.com'

with open(sys.argv[1]) as input_file:
    with open(sys.argv[2], "w") as output_file:
        number_of_examples = int(input_file.readline())

        for case_number in xrange(1, number_of_examples+1):
            num_of_bits, num_of_coins = (int(number) for number in input_file.readline().rstrip("\n").split(" "))

            # The first and last number must be 1.
            num_of_bits -= 2
            format_string = '0%sb' % num_of_bits

            def get_first_divisor(number):
                # 1 is technically not a prime. Not sure how this is handled in this Jam. "1" is a valid coin.
                if number == 1:
                    return 1

                # Except for one, all other number below 4 do not have a non-trivial divisor.
                if number < 4:
                    return 0

                # All even numbers are dividable by 2.
                if not number & 1:
                    return 2

                # Check all odd numbers up to the square root.
                for divisor in range(3, int(math.floor(math.sqrt(number)))+1, 2):
                    if number % divisor == 0:
                        return divisor

                # Number is a prime. No divisor found.
                return 0

            def get_divisors_in_all_bases(value):
                divisors_in_bases = []
                # Check all the bases.
                for base in xrange(2, 11):
                    value_in_base = int(value, base)
                    divisor = get_first_divisor(value_in_base)
                    if divisor:
                        divisors_in_bases.append(divisor)
                    else:
                        return []
                return divisors_in_bases

            output_file.write("Case #%d:\n" % case_number)

            coin_counter = 0
            for middle_coin_value in xrange(0, pow(2, num_of_bits)):
                coin = '1%s1' % format(middle_coin_value, format_string)
                divisors = get_divisors_in_all_bases(coin)
                if divisors:
                    coin_counter += 1
                    output_file.write("%s %s\n" % (coin, " ".join(str(x) for x in divisors)))
                    # Enough coins.
                    if coin_counter == num_of_coins:
                        break
