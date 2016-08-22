import math

T = input("Input T: ")

S = [''] * T
print "Input N: "
for i in range(0, T):
    S[i] = raw_input()

Flips = [0] * T
for i in range(0, T):
    if len(S[i]) == 1:
        if S[i][0] == '+':
            Flips[i] = 0
        else:
            Flips[i] = 1
        continue

    for j in range(1, len(S[i])):
        if S[i][j] != S[i][j-1]:
            Flips[i] += 1

    if S[i][len(S[i])-1] == '-':
        Flips[i] += 1


for i in range(0, T):
    print "Case #", i+1, ":", Flips[i]
