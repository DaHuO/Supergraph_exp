#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1

def get_nontrivial_diviser(x):
    if x <= 2: return 0
    if x&1 == 0: return 2
    i = 3
    #while i**2 <= x:
    while i <= 100:
        if x%i == 0: return i
        i += 2
    return 0

def solve(N, J):
    answers = []
    for i in xrange(1<<(N-1),pow(2,N)):
        if i&1 == 0:
            continue

        digits = bin(i)[2:]
        divisers = []
        for j in range(2, 11):
            n = get_nontrivial_diviser(int(digits, j))
            if n == 0:
                # not coin jam
                break
            else:
                divisers.append(n)
        else:
            # coin jam!
            answers.append(digits + ' ' + ' '.join(map(str, divisers)))
            if len(answers) == J:
                return answers

    return ['000']*J

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for i in range(num_of_case):
        (N, J) = map(int, f.readline().rstrip().split())
        answers = solve(N, J)
        
        print "Case #%d:" % (i+1)
        for j in range(J):
            print answers[j]


