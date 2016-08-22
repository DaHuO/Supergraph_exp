T = int(raw_input())
for t0 in xrange(1, T+1):
    N = list(raw_input())

    L = len(N)
    count = 0
    last_minus = -1

    for i in xrange(L-1, -1, -1):
        if N[i] == '-':
            last_minus = i
            break

    if last_minus == -1:
        print "Case #"+str(t0)+":", count
        continue

    while N[last_minus] == '-':
        count += 1
        first_sign = N[0]
        for i in xrange(L):
            if N[i] == first_sign:
                if N[i] == '+':
                    N[i] = '-'
                else:
                    N[i] = '+'
            else:
                break

    print "Case #"+str(t0)+":", count