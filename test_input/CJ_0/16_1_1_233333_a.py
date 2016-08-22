import sys

input = sys.stdin.readlines()


for i in xrange(1,len(input)):
    l = []
    s = input[i].strip('\n')
    res = str(s[0])
    for c in s[1:]:
        if c >= res[0]:
            res = str(c)+res
        else:
            res += str(c)
            
    print 'Case #'+str(i)+': ' + res

