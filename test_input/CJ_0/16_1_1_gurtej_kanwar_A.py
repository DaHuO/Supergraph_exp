import sys

T = int(sys.stdin.readline())

for i in range(T):
    word = sys.stdin.readline().strip()
    cur = []
    for c in word:
        if len(cur) == 0:
            cur.append(c)
        else:
            if ord(c) >= ord(cur[0]):
                cur.insert(0, c)
            else:
                cur.append(c)
    print "Case #%d: %s" % (i+1, "".join(cur))
