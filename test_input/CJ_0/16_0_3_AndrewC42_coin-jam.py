import string

def int_to_base(num, base):
    # check for invalid base
    if base < 2 or base > 10:
        raise Exception("int_to_base requires a base between 0 and 10")

    if num < 0:
        finalnum = "-"
        num = num*-1
    else:
        finalnum = ""

    if num == 0:
        return 0

    maxpower = 0
    while(True):
        if base**(maxpower + 1) > num:
            break
        maxpower += 1
        # print "maxpower: {}, base: {}, num: {}".format(maxpower, base, num)

    for i in range (maxpower, -1, -1):
        # print "maxpower is {}, finalnum is {}, num is {}, result is {}, base is {}".format(maxpower, finalnum, num, int(num/(base**i)), base)
        finalnum += str(int(num/(base**i)))

        num = num%(base**i)

    return int(finalnum)

def base_to_int(num, base):
    finalnum = 0
    length = len(str(num))
    for i in range(length):
        finalnum += int(str(num)[i]) * (base**(length-i-1))
    return int(finalnum)

def binary_to_base10(num):
    power = len(str(num)) - 1
    base10num = 0
    for digit in str(num):
        base10num += (int(digit) * (2**power))
        power -= 1
    return base10num

# return any non-trivial divisors for a number. If number is prime, return -1
def nontrivial_divisor(num):
    # if the number is even, return 2 as the non-trivial divisor
    if num % 2 == 0:
        return 2
    # no odd number from 1 to 9 has a non-trivial divisor (1 included)
    if num < 9:
        return -1
    # divide by all odds before square root point to find a divisor
    halfpoint = int(num**0.5)
    # print "--{}, halfpoint is {}".format(num, halfpoint)
    for i in range(3, halfpoint + 2, 2):
        if num%i == 0:
            return i
    # after this loop the number must be prime, so return -1 to signify this
    return -1

def main():
    tests = int(raw_input())
    for i in range(1, tests + 1):
        length, jamcoins = [int(s) for s in raw_input().split(" ")]
        print "Case #{}:".format(i)

        # saves the highest number in between the starting and finishing 1's
        # that is reached in the following for loop
        current_middle_jamnum = -1

        for k in range(jamcoins):

            if current_middle_jamnum >= 2**(length-2):
                break

            # Loop over all possible combination of numbers in between the
            # starting and finishing 1's.
            # Searches from where the previous jamnum was found onwards
            for current_middle_jamnum in range(current_middle_jamnum + 1, 2**(length-2)):
                # generate jamnum
                jamnum = int_to_base(current_middle_jamnum, 2)
                jamnum = (jamnum * 10) + 1      # add 1 to end
                jamnum = jamnum + 10**(length-1)    # add 1 to start

                # loop over each base
                failure = False
                divisors = []
                for base in range(2, 11):
                    # find the number's representation in that base
                    jamnum_base = base_to_int(jamnum, base)
                    # print "Jamnum {} in base {} is {}".format(jamnum, base, jamnum_base)
                    # check if prime and add divisor to list
                    divisor = 0
                    divisor = nontrivial_divisor(jamnum_base)
                    if divisor == -1:
                        failure = True
                        break
                    else:
                        # print "Divisor for {} is {}".format(jamnum_base, divisor)
                        divisors.append(divisor)

                if not(failure):
                    print jamnum,
                    for n in range(len(divisors)):
                        print divisors[n],
                    print
                    break


main()
