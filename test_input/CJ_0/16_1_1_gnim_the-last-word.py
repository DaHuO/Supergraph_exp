def last(S):
    rst = ""
    for char in S:
        rst =  char + rst if char + rst > rst + char else rst + char
    return rst


T = int(raw_input())

for t in range(1, T+1):
    S = raw_input()
    print "Case #" + str(t) + ": " + last(S)
