import sys

def find(s) :
    s = s.replace("\n", "")
    ret = ""

    for c in s :
        if len(ret) == 0 :
            ret += c
            continue
        if c < ret[0] :
            ret = ret+c
        else :
            ret = c+ret

    return ret

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    #print(T)
    for i in range(T) :
        s = sys.stdin.readline()
        res = find(s)
        print "Case #%d: %s" % (i+1, res)
