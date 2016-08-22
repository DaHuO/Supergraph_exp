def last_minus(S):
    for i in reversed(range(len(S))):
        if S[i] == '-':
            # print "%s last minus % s" % (S, i)
            return i+1
    # print "%s last minus % s" % (S, len(S))
    return 0


def flipped(S):
    return map(lambda c: "+" if c == '-' else '-', reversed(S))


def flips_for(S):
    # print "flips for % s" % S
    if not S:
        return 0
    # S is nonempty
    if S[-1] == '+':
        return flips_for(S[:last_minus(S)])
    # S ends with '-'
    if S[0] == '-':
        # flip all
        return 1 + flips_for(flipped(S))
    # S ends with '-' and starts with '+'; flip all top pluses
    for i in range(len(S)):
        if S[i] == '+':
            S[i] = '-'
        else:
            break
    return 1 + flips_for(S)


T = int(raw_input())
for i in range(T):
    S = list(raw_input())
    # print "case %d" % i
    print "Case #%d: %s" % (i + 1, flips_for(S))