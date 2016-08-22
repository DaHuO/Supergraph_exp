import sys

T = int(sys.stdin.readline())

for t in range(T):
    stack = sys.stdin.readline().strip()
    cur = '+'
    count = 0
    for c in stack[::-1]:
        if c != cur:
            count += 1
            cur = c

    print("Case #{}: {}".format(t+1, count))

