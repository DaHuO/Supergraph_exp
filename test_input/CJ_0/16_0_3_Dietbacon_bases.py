import itertools
import math

def is_prime(n):
    if n == 2:
        return None
    if n % 2 == 0:
        return 2

    sqr = int(math.sqrt(n)) + 1
    divisor = 3
    while divisor < sqr and divisor < 10000000:
        if n % divisor == 0:
            return divisor
        divisor += 2
    return None

def is_coin(nbr_str):
    divisor_list = [0 for i in range (1,10)]
    for i in range(2, 11):
        nbr_in_base = int(nbr_str, i)
        prime = is_prime(nbr_in_base)
        if not prime:
            return 0
        else:
            divisor_list[i - 2] = prime
    for i in range (0, len(divisor_list)):
        divisor_list[i] = str(divisor_list[i])
    print nbr_str + ' ' + ' '.join(divisor_list)
    return 1

def willit(ones, length, cases_found, qty):
    one_positions = itertools.combinations([i for i in range(1, 16)], ones)
    i = 0
    for comb in one_positions:
        i += 1
        nbr_list = ['1'] + ((length - 2) * ['0']) + ['1']
        for pos in comb:
            nbr_list[pos] = '1'
        nbr_str = ''.join(nbr_list)
        if is_coin(nbr_str):
            cases_found += 1
        if cases_found == qty:
            return cases_found
    return cases_found

def case(length, qty):
    cases_found = 0
    base_str = (length - 2) * '0'
    base_list = list(base_str)
    for i in range(0, length - 1, 2):
        cases_found = willit(i, length, cases_found, qty)
        if cases_found == qty:
            break
    if cases_found < qty:
        for i in range(1, length - 1, 2):
            cases_found = willit(i, length, cases_found, qty)
            if cases_found == qty:
                break

def main():
    cases = int(raw_input())
    for i in range(1, cases + 1):
        print 'Case #' + str(i) + ':'
        case_params = raw_input()
        case_params = case_params.split()
        length = int(case_params[0])
        qty = int(case_params[1])
        case(length, qty)
main()
