import sys

def find(s) :
    ret = 0
    n = len(s)
    #print n
    if n == 2 and s[0] == '+' :
        return 0
    elif n == 2 and s[0] == '-':
        return 1
    cond = 1
    i = 0
    #return 10
    while True :
        b = 0
        for i in range(len(s)-1) :
            if s[i] != s[i+1] :
                b = i
                break
        if i+2 == n and s[0] == '+':
            break
        newS = ''
        for j in range(i+1) :
            if s[j] == '+' :
                newS += '-'
            else :
                newS += '+'
        newS += s[i+1:]
        #print i,s, newS
        s = newS
        ret += 1
        

    return ret

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    #print(T)
    for i in range(T) :
        s = sys.stdin.readline()
        res = find(s)
        print "Case #%d: %s" % (i+1, res)
