T = int(input())

for t in range(1, T+1):
    S = input()

    flips = 0
    for i in range(1, len(S)):
        if S[i] != S[i-1]:
            flips += 1

    if S[-1] == '-':
        flips += 1

    print("Case #{0}: {1}".format(t, flips))
