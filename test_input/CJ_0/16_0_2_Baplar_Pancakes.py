import sys
import os
import math

def permuter(car) :
    if car == "+" :
        return "-"
    else :
        return "+"

def flip(pancakes, N) :
    center = int(N/2)
    for i in range(center) :
        tmp = permuter(pancakes[N-1-i])
        pancakes[N-1-i] = permuter(pancakes[i])
        pancakes[i] = tmp
    if N%2 == 1 :
        pancakes[center] = permuter(pancakes[center])

def reduce(pancakes) :
    while len(pancakes) > 0 and pancakes[-1] == "+" :
        pancakes.pop()

def happy(string) :
    ops = 0
    pancakes = list(string)
    reduce(pancakes)
    L = len(pancakes)
    while L > 0 :
        i = 0
        while i < L and pancakes[i] == "+" :
            i += 1
        if i > 0 :
            flip(pancakes, i)
            ops += 1
        if i < L :
            flip(pancakes, L)
            ops += 1
        reduce(pancakes)
        L = len(pancakes)
    return ops


if (len(sys.argv) < 2) :
    print("No input filename given.", file = sys.stderr)
    sys.exit(1)

input_filename = sys.argv[1]
if (len(sys.argv) > 2) :
    output_filename = sys.argv[2]
else :
    output_filename = os.path.splitext(input_filename)[0] + ".out"

try:
    input_file = open(input_filename, 'r')
except IOError:
    print("Unable to open " + input_filename + " for input.", file = sys.stderr)
    sys.exit(1)

try:
    output_file = open(output_filename, 'w')
except IOError:
    print("Unable to open " + output_filename + " for output.", file = sys.stderr)
    sys.exit(1)

T = int(input_file.readline().rstrip())

for cas in range(1, T+1) :
    string = input_file.readline().rstrip()
    Res = happy(string)
    output_file.write("Case #" + str(cas) + ": " + str(Res) + "\n")

input_file.close()
output_file.close()
