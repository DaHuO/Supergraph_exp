#!/usr/bin/python

from sys import stdin, stdout

T = int(stdin.readline().strip())

# def count_ones(s):
#     return sum(map(int, s))

def to_base(n, b):
    s = []
    while n > 0:
        r = n % b
        s.append(str(r))
        n = n // b
    s.reverse()
    return ''.join(s)

for case_num in range(1, T+1):
    N,J = [ int(n) for n in stdin.readline().strip().split() ]
    answers = []
    divisors_list = []
    n = '10000000000000000000000000000001'
    while len(answers) < J:
        divisors = []
        for b in range(2,10+1):
            n_b = int(n, b)
            found = False
            for d in [2,3,5,7,11,13,17]:
                if n_b % d == 0:
                    divisors.append(d)
                    found = True
                    break
            if not found:
                break
        if found:
            answers.append(n)
            divisors_list.append(divisors)
        n = to_base(int(n,2)+2, 2)

    stdout.write("Case #{:d}:\n".format(case_num))
    for i in range(J):
        stdout.write("{0:s} {1[0]:d} {1[1]:d} {1[2]:d} {1[3]:d} {1[4]:d} {1[5]:d} {1[6]:d} {1[7]:d} {1[8]:d}\n".format(answers[i], divisors_list[i]))
