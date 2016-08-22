test_input = \
"""8
CAB
JAM
CODE
ABAAB
CABCBBABC
ABCABCABC
ZXCASDQWE
B"""
test_output = \
"""Case #1: CAB
Case #2: MJA
Case #3: OCDE
Case #4: BBAAA
Case #5: CCCABBBAB
Case #6: CCCBAABAB
Case #7: ZXCASDQWE
Case #8: B"""

import itertools
import math
import sys
test = False
line_number = 0


def get_numbers(input_number, previously_seen):
    for i in range(0, 10):
        if str(i) not in previously_seen and str(i) in str(input_number):
            previously_seen.add(str(i))


def get_input():
    global line_number
    if not test:
        return raw_input("")
    else:
        output = test_input.split("\n")[line_number]
        line_number += 1
        return output

if __name__ == "__main__":
    cases = int(get_input())
    for case in range(cases):
        word = get_input()
        # basically we need to optimize the insertion of each letter
        # simple rule: if putting it on the left would generate a higher number than putting it on the right, do it, otherwise right
        output = ""
        if len(word) == 1:
            output = word
        else:
            for letter in word:
                if len(output) == 0:
                    output += letter
                else:
                    if ord(letter) >= ord(output[0]):
                        output = letter + output
                    else:
                        output += letter

        print "Case #{}: {}".format(case + 1, output)


