T = int(raw_input())

for i in range(T):
    seq = raw_input()
    d = 1
    ret = 0
    for c in seq[::-1]:
        if c == '-' and d == 1:
            d = 0
            ret += 1
        elif c == '+' and d == 0:
            d = 1
            ret +=1

    print "Case #%d: %d" % (i+1, ret)


            
