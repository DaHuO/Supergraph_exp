T = int(input())

for t in range(1, T+1):
    pancakes = [int(x == '+') for x in input()]
    a = 1
    n = 0
    for x in range(len(pancakes) - 1, -1, -1):
        if pancakes[x] != a:
            a = pancakes[x]
            n += 1

    print("Case #{0}: {1}".format(t, n))
