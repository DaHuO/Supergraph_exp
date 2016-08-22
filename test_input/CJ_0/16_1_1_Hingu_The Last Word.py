def checkLast(s1, s2):
    if s1[0] > s2[0]:
        return s1
    return s2

def main():
    for t in xrange(int(raw_input().strip())):
        s = raw_input().strip()
        output = s[0]
        for i in range(1, len(s)):
            s1 = output + s[i]
            s2 = s[i] + output
            output = checkLast(s1, s2)
        print 'Case #'+str(t+1)+':', output

if __name__ == '__main__': 
    main()
