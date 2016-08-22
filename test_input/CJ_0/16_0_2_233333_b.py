import sys

input = sys.stdin.readlines()

def flip(s):
    if len(s) == 0:
        return s
    s1 = s[::-1]
    
    s_new = ''
    
    for c in s1:
        if c=='-':
            s_new += '+'
        elif c == '+':
            s_new += '-'
    return s_new


def do(s, count):
    #print s
    if not '-' in s:
        return count
    
    if s[0] == '+':
        j = 0
        for i in xrange(len(s)):
            if s[i] == '-':
                s_new = flip(s[0:i]) + s[i:]
                #print s_new
                break
        return do(s_new, count+1)

    if s[-1] == '-':
        return do(flip(s), count+1)
    
    for i in xrange(len(s)-1,-1,-1):
        if s[i] == '-':
            return do(flip(s[0:i+1]), count+1)
                
    

for i in xrange(1,len(input)):
    s = input[i].strip('\n')
    
    print 'Case #'+str(i)+': ' + str(do(s,0))
    
    #print flip('--+-')
    
    #print do(s, 0)
