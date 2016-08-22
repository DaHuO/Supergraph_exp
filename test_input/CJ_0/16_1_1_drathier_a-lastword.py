"""
add letter in front, back
"""

import sys

sys.setrecursionlimit(10000)


def solve2(s, word):
    # print "a", s, word
    if s == "":
        return word
    if s[0] + word < word + s[0]:
        return solve2(s[1:], word + s[0])
    else:
        return solve2(s[1:], s[0] + word)


def m():
    n = input()
    a = []
    for _ in range(n):
        a += [raw_input()]

    #print "input", a
    num = 1
    for i in a:
        print "Case #{0}: {1}".format(num, solve2(i, ""))
        num += 1


m()
