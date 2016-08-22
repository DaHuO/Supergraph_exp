def f(S):
    builder = ''
    for c in S:
        if builder == '':
            builder = c
        else:
            if c >= builder[0]:
                builder = c + builder
            else:
                builder = builder + c
    return builder

T = int(raw_input())
for t in xrange(1, T + 1):
    S = raw_input()
    print 'Case #{}: {}'.format(t, f(S))
