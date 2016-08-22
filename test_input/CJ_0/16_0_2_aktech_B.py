"""
Google Code Jam 2016
Problem B. Revenge of the Pancakes
Author: Amit Kumar | dtu.amit@gmail.com
"""


def solve(s):
    count = 0
    for i in range(len(s)):
        if (i != len(s) - 1) and (s[i] != s[i + 1]):
            count += 1
    if s[len(s) - 1] == '-':
        count += 1
    return count

T = int(input())

for i in range(1, T + 1):
    s = raw_input()
    print ("Case #%s: %s" % (i, solve(s)))
