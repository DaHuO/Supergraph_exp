#!/usr/bin/env python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

"""
Solution to Codejam 2016 a - the last word

Given a string S, one letter at a time, put the letters on the front or back such that the 
final string is the last possible word in alphabetical order for that string
"""

import sys

class LastWord(object):
    def __init__(self):
        self.word = ""

    def add_char(self, char):
        """Add the character."""
        if self.word == "":
            self.word = char
        elif char > self.word[0] or char == self.word[0]:
            self.word = char + self.word
        else:
            self.word += char


if __name__ == "__main__":
    in_file = open(sys.argv[1], 'r')
    out_file = open(sys.argv[2], 'w')

    case_count = int(in_file.readline())
    for i in range(case_count):
        player = LastWord()
        S = in_file.readline().strip()
        for c in S:
            player.add_char(c)
        out_file.write("Case #{}: {}\n".format(i + 1, player.word))

    in_file.close()
    out_file.close()
