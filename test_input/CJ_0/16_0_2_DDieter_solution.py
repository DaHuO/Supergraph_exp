import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

T = int(input())

for t in range(1, T+1):
    S = input().strip()
    flips = 0
    while "-" in S:
        index = S.rindex("-")
        newS = ""
        for i in range(index + 1):
            newS += "+" if S[i] == "-" else "-"
        S = newS + S[index + 1:]
        flips += 1

    print("Case #" + str(t) + ": " + str(flips))