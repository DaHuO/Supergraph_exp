from __future__ import division, print_function, unicode_literals

import fileinput

def counting_sheep(N):
    '''
    Code Jam 2016, Qualification Round, Problem A
    '''
    digits = set(range(10))
    for i in range(1, int(1e6)):
        number = i*N
        digits.difference_update([int(x) for x in str(number)])
        if not digits:
            return number
    return 'INSOMNIA'

def revenge_of_the_pancakes(pancakes):
    '''
    Code Jam 2016, Qualification Round, Problem B
    '''
    last_pancake = '+'
    n_maneuver = 0
    for pancake in reversed(pancakes):
        if pancake == last_pancake:
            pass
        else:
            n_maneuver += 1
            last_pancake = pancake
    return n_maneuver

if __name__ == '__main__':
    for i, line in enumerate(fileinput.input()):
        if i == 0:
            continue
        index = i
        pancakes = list(line.strip())
        answer = revenge_of_the_pancakes(pancakes)
        print("Case #{index}: {answer}".format(index=index, answer=answer))
