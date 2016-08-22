from __future__ import division, print_function, unicode_literals

import fileinput
import collections

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

def the_last_word(letters):
    '''
    Code Jam 2016, Round 1A, Problem A
    '''
    if not letters:
        return ''
    last_word = collections.deque([letters[0]])
    for character in letters[1:]:
        if ord(character) < ord(last_word[0]):
            last_word.append(character)
        else:
            last_word.appendleft(character)
    return ''.join(last_word)


if __name__ == '__main__':
    input = fileinput.input()
    n_case = int(input.readline())
    for i in range(n_case):
        letters = input.readline().strip()
        answer = the_last_word(letters)
        print('Case #{}: {}'.format(i+1, answer))
