from math import sqrt
from random import choice

## Chm, pro velky dataset to rychle naslo nasledujici a pak pul hodiny nic...
#1 | 11100000001000010111011111101011 : [7, 7, 4623043, 79, 907, 109, 163753, 7, 7]
#2 | 11010001001111111001001001110001 : [3, 59, 7, 3, 53, 17, 3, 7039, 59]
#3 | 10001010000000111000111000100011 : [3, 2, 3, 2, 1151, 2, 3, 2, 3]
#4 | 10111011101110001111001011000011 : [421, 13, 5, 977, 17, 173, 14051, 5, 19]
#5 | 11011000100001100010100101101001 : [13, 2, 7, 2, 13, 2, 7, 2, 271]
#6 | 10110011011001101011001110111001 : [3, 13, 23, 3, 89, 5, 3, 16729591, 937]


# Pozorovani:
# - vyhodnocovani nekterych cisel, zejmena prvocisel (ktera me nezajimaji) trva
# desne dlouho - takova cisla je dobra co nejdriv odriznout (i kdyz by mohly
# byt potencialne jamcoiny (viz max_limit nize))

def main(length=32, count=500):
    #print(nontrivial_divisors_for_all_bases('10110011011001101011001110110101'))
    solutions = solve(length, count)
    output_solutions(solutions)

def solve(length, count):
    #print(nontrivial_divisors_for_all_bases('100011'))
    solutions = {}
    while len(solutions) < count:
        coin = '1' + ''.join(choice(['0', '1']) for i in range(length-2)) + '1'
        divisors = nontrivial_divisors_for_all_bases(coin)
        if divisors and coin not in solutions:
            solutions[coin] = divisors
            print(len(solutions), '|', coin, ':', divisors)
    return solutions



def output_solutions(solutions):
    #print('Case #1:')
    #for jamcoin, divisors in solutions.items():
    #    print(jamcoin, *divisors)
    with open('output', 'w') as f:
        f.write('Case #1:\n')
        for jamcoin, divisors in solutions.items():
            f.write('{coin} {divisors}\n'.format(coin=jamcoin,
                divisors=' '.join(map(str, divisors))))


def nontrivial_divisors_for_all_bases(coin):
    divisors = []
    for base in range(2, 11):
        divisor = nontrivial_divisor_for_base(coin, base)
        if divisor is None:
            return None
        else:
            divisors.append(divisor)
    return divisors


def nontrivial_divisor_for_base(coin, base):
    number = int(coin, base)
    return nontrivial_divisor(number)


def nontrivial_divisor(n, max_divisor=100000):
    """ Return nontrivial divisor, or None, if n is prime (or 1)

    Also returns None if it computers too long (if actual divisor > max_divisor)
    """
    if n < 4:
        return None
    elif n % 2 == 0:
        return 2
    elif n < 9:
        return None
    elif n % 3 == 0:
        return 3
    else:
        limit = min(max_divisor, int(sqrt(n)))
        divisor = 5
        while divisor <= limit:
            if n % divisor == 0:
                return divisor
            if n % (divisor + 2) == 0:
                return (divisor + 2)
            divisor += 6
        return None


if __name__ == '__main__':
    main()
