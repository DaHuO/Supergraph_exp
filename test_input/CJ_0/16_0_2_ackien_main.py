#!/usr/bin/python

from sys import stdin, stdout

T = int(stdin.readline().strip())

for case_num in range(1, T+1):
    pancakes = stdin.readline().strip()
    i = 1
    total = 0
    while i < len(pancakes):
        if pancakes[i-1] != pancakes[i]:
            total += 1
        i += 1
    if pancakes[len(pancakes)-1] == '-':
        total += 1
    answer = str(total)
    stdout.write("Case #{:d}: {:s}\n".format(case_num, answer))
