#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(cipher):
    size = len(cipher)
    number_checked = 0
    moves = 0
    if cipher[0] == '-':
        try:
            next_happy = cipher.index('+')
            flipped_blanks = '+' * next_happy
            cipher = flipped_blanks + cipher[next_happy:]
            number_checked = next_happy
            moves += 1
        except ValueError:  # only '-'s left
            moves += 1
            return str(moves)
    while number_checked < size:
        try:
            next_blank = cipher.index('-')
            try:
                rest_of_string = cipher[next_blank:]
                try:
                    next_happy = rest_of_string.index('+')
                    total_index = cipher.index(rest_of_string) + next_happy
                    flipped = '+' * (total_index+1)
                    cipher = flipped + cipher[total_index + 1:]
                    moves += 2
                    number_checked = total_index
                except ValueError:
                    return moves + 2
            except IndexError:
                return moves + 2
        except ValueError:
            return moves
    return moves


if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases + 1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
