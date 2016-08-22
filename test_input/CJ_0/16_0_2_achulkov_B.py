__author__ = 'Andrey'
import sys

fin = open("B-large.in", "r")
fout = open("output.txt", "w")


s = ""


def solve(i, side):
    if i == -1:
        return 0
    else:
        if s[i] == "+":
            if side:
                return solve(i - 1, True)
            else:
                return 1 + solve(i - 1, True)
        elif s[i] == "-":
            if side:
                return 1 + solve(i - 1, False)
            else:
                return solve(i - 1, False)


t = int(fin.readline().rstrip())
for i in range(1, t + 1):
    s = fin.readline().rstrip()
    fout.write("Case #" + str(i) + ": " + str(solve(len(s) - 1, True)) + "\n")