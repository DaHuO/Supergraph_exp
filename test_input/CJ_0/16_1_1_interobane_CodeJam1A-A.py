#!/usr/bin/env python

# import sys

def solve(s):
    if len(s) < 1:
        return 'INVALID'
    elif len(s) == 1:
        return s
    letters = list(s)
    el = letters.pop(0)
    while len(letters) > 0:
        next_letter = letters.pop(0)
        if el[0] > next_letter:
            el += next_letter
        else:
            el = next_letter + el
    return el

def main():
    num_cases = raw_input()
    # sys.stderr.write('Number of cases: ' + num_cases + '\n')
    for i in range(int(num_cases)):
        s = raw_input()
        # sys.stderr.write(s + '\n')
        answer = solve(s)
        print('Case #{0}: {1}'.format(i+1, answer))

if __name__ == '__main__':
    main()
