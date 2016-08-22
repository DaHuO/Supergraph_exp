import os, sys
import collections as coll
import functools as ft
import itertools as it

# get problem letter from script name
problem_letter = sys.argv[0].split('.')[0]
data_set = sys.argv[1]
attempt_number = sys.argv[2]

input_filename = "%s-%s-%s.in" % (problem_letter, data_set, attempt_number)
input_file = open(input_filename)
lines = [line[:-1] for line in input_file.readlines()[1:]][:]

output_filename = "%s.out" % problem_letter
output_file = open(output_filename, "w+")
#sys.stdout = output_file


def get_chunks(lines, n):
    for i in range(0, len(lines), n):
        yield lines[i:i+n]

from jamcode import *
lines_per_case = 2
chunks = get_chunks(lines, lines_per_case)

jamcoins = []

mults = []
for n in range(2,11):
    values = [1] + [n**x for x in range(1,16)]
    mults.append(list(reversed(values)))

def get_divisor(num):
    for i in range(3,int(num**0.5)+1):
        if num%i == 0:
            return i
    return False

def is_jam(num):
    proof = []
    inner = num[1:-1]
    num_len = len(num)
    for mult in mults:
        compressed = list(it.compress(mult[-num_len:], [1] + map(int, inner) + [1]))
        value = sum(compressed)
        divisor = get_divisor(value)
        if divisor:
            proof.append(divisor)
        else:
            return False
    jamcoins.append(num)
    return proof

def get_answer(chunk):
    N, J = map(int, chunk[0].split(' '))
    answers = []
    c = 0
    digitsets = it.product(range(2), repeat=N-2)
    for digitset in digitsets:
        num = "1%s1" % "".join(map(str,digitset))
        if num not in jamcoins:
            proof = is_jam(num)
            if proof:
                answers.append("%s %s" % (num, " ".join(map(str,proof))))
                c += 1
        if c >= J:
            return "\n" + "\n".join(answers)

for i, chunk in enumerate(chunks):
    print "Case #%s: %s" % (i+1, get_answer(chunk))

input_file.close()
output_file.close()
