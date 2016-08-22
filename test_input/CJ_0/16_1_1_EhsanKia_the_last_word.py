from collections import deque

T = int(raw_input())

for case in range(T):
    S = raw_input().strip()

    q = deque()

    for c in S:
        if not q:
            q.append(c)
            continue

        if c >= q[0]:
            q.appendleft(c)
        else:
            q.append(c)

    print "Case #{}: {}".format(case + 1, ''.join(q))
