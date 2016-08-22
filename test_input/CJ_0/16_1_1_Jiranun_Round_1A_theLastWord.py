__author__ = 'Jiranun.J'

n_test_case = int(raw_input())  # read a line with a single integer

for i in range(n_test_case):
    S = raw_input()
    result = S[0]

    for c in range(1, len(S)):
        if ord(S[c]) >= ord(result[0]):
            result = S[c]+result
        else:
            result = result+S[c]

    print 'Case #'+str(i+1)+': '+result




