from itertools import groupby

T = int(raw_input())

for case in range(T):
    S = raw_input()

    groups = [k for k, g in groupby(S)]

    if len(groups) == 1:
        answer = 1 if groups[0] == '-' else 0
    else:
        answer = len(groups) if groups[-1] == '-' else len(groups) - 1

    print "Case #%d: %d" % (case+1, answer)