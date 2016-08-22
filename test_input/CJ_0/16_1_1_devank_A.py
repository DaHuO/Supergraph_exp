t = int(raw_input())
for i in xrange(1, t + 1):
    s = raw_input()
    first = s[0]
    last = s[0]
    output = ""
    output = output + s[0]
    for j in range(1,len(s)):
        if(s[j]<last or s[j]<first):
            output = output + s[j]
            last = s[j]
        else:
            output = s[j] + output
            first = s[j]

    print "Case #{}: {}".format(i,output)