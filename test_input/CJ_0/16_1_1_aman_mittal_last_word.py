T = int(raw_input())
for i in range(T):
    S = raw_input().strip()
    res = ''
    for x in S:
        if len(res) != 0 and ord(x) >= ord(res[0]):
            res = x + res
        else:
            res += x
    print "Case #{0}: {1}".format(i+1, res)

