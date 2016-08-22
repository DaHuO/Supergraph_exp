def increase(digits):
    if 0 not in digits:
        return None
    else:
        index = len(digits)-1
        while digits[index] == 1:
            digits[index] = 0
            index -= 1
        digits[index] = 1
        return digits


def get_interpretation(digits, base):
    x = 0
    for exp in range(0,len(digits)):
        digit = digits[len(digits)-1-exp]
        x += digit * pow(base, exp)
    return x


def get_divisor(x):
    for divisor in range(2, 23):
        if x % divisor == 0:
            return divisor
    return x


def main():
    _ = input()
    [n, j] = [int(x) for x in input().split()]
    print ("Case #1:")

    digits = [1]+[0]*(n-2)+[1]
    found_jamcoins = 0
    while digits and found_jamcoins < j:
        # check that the digits end with 1
        if digits[-1] == 0:
            digits = increase(digits)
        # get the divisors
        divisors = []
        is_jamcoin = True
        for base in range(2,11):
            interpretation = get_interpretation(digits, base)
            divisor = get_divisor(interpretation)
            if divisor == interpretation:
                is_jamcoin = False
                break
            else:
                divisors.append(divisor)

        if is_jamcoin:
            found_jamcoins += 1
            digits_str = "".join([str(d) for d in digits])
            divisors_str = " ".join([str(d) for d in divisors])
            print (digits_str+ " "+divisors_str)
        digits = increase(digits)

main()