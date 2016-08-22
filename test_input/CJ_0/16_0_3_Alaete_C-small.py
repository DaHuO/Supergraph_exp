infile = open("C-small-attempt1.in", "r")
cases = infile.readline()
line = infile.readline()
length = int(line[0:2])
numbers = int(line[3:5])
infile.close()

import itertools
import random
from math import gcd

def Factor(N):
    if N == 1:
        return N
    if N % 2 == 0:
        return 2
    y, c, m = random.randint(1, N - 1), random.randint(1, N - 1), random.randint(1, N - 1)
    g, r, q = 1, 1, 1
    while g == 1:
        x = y
        for i in range(r):
            y = ((y * y) % N + c) % N
        k = 0
        while (k < r and g == 1):
            ys = y
            for i in range(min(m, r - k)):
                y = ((y * y) % N + c) % N
                q = q * (abs(x - y)) % N
            g = gcd(q, N)
            k = k + m
        r = r * 2
    if g == N:
        while True:
            ys = ((ys * ys) % N + c) % N
            g = gcd(abs(x - ys), N)
            if g > 1:
                break
    return g

def Base(number, base):
    interpretation = 0
    digits = list(number)
    digits.reverse()
    for i in range(len(digits)):
        interpretation += int(digits[i])*(int(base)**i)
    return interpretation

def Jamcoin_Check(number):
    interpretations = []
    for i in range(2, 11):
        if Factor(Base(number, i)) == (Base(number, i)):
            return False, False
        else:
            interpretations.append(str(Factor(Base(number, i))))
    return True, interpretations

possible = []
proven = []

for value in list(["".join(seq) for seq in itertools.product("01", repeat=int(length-2))]):
    possible.append("1" + value + "1")

outfile = open("C-small-output.txt", "a")
outfile.write("Case #%s:\n" % cases)
count = 0
for value in possible:
    if count == int(numbers):
        break
    else:
        if Jamcoin_Check(value)[0] == True:
            outfile.write((("%s %s\n") % (value, ' '.join(Jamcoin_Check(value)[1]))))
            count += 1
outfile.close()