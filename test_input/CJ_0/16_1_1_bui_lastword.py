t = int(raw_input())

for caseNumber in range(1, t+1):
    s = list(raw_input())

    for idx, eachChar in enumerate(s):
        if ord(eachChar) >= ord(s[0]):
            s.pop(idx)
            s.insert(0, eachChar)

    print "Case #{}: {}".format(caseNumber, ''.join(s))