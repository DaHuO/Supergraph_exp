import itertools, math

def convert_to_base(two, base):
    result = 0
    two = two[::-1]
    i = 0
    multiplier = base
    base = 1
    while i < len(two):
        result += int(two[i]) * base
        base *= multiplier
        i += 1

    return result

def is_prime(number, numbers):
    for divider in range(2, int(math.sqrt(number)) + 1):
        if number % divider == 0:
            if not divider in numbers:
                dividers.append(divider)
                return False
        if divider > 10000:
            return True

    return True

def calc_perm(number_of_0, number_length):
    if number_of_0 < 3:
        yield permutation(number_of_0, 1, number_length)

    for k in range(number_of_0, 1, -1):
        yield permutation(k, number_of_0 - k + 1, number_length)

def permutation(number_of_0, number_of_1, number_length):
    str_with_0 = '0' * number_of_0 + '1' * number_of_1
    for perm in itertools.permutations(str_with_0, len(str_with_0)):
        for i in range(0, number_length - len(str_with_0) + 1):
            number = [1] * number_length
            for j in range(len(str_with_0)):
                number[j+i] = perm[j]
            yield "".join(map(str, number[::-1]))

try:
    for iteration in range(int(input()), int(1) + 1):
        n, j = map(int, input().strip().split(" "))
        initial_setup = [1] * n
        print("Case #{0}: ".format(iteration))
        already_printed = []
        total = 0
        for i in range(0, n-1):
            for p in calc_perm(i, n-2):
                for perm in p:
                    numbers = []
                    dividers = []
                    for base in range(2, 11):
                        str_num = "1" + perm + "1"
                        numbers.append(convert_to_base(str_num, base))
                    for number in numbers:
                        if is_prime(number, numbers):
                            break
                    else:
                        if str_num in already_printed:
                            continue
                        else:
                            already_printed.append(str_num)
                            print(str_num, " ".join(map(str, dividers)))
                            total += 1
                            if total == j:
                                raise StopIteration
except StopIteration: pass