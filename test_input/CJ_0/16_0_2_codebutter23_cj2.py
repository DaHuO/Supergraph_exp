t=input()
def panc(t):
    for i in range(1,t+1):
        s=raw_input()
        if '-' not in s:
            print "Case #" + str(i) + ": " + str(0)
            continue
        if '+' not in s:
            print "Case #" + str (i) + ": " + str(1)
            continue
        ctr=0
        while s!= '+'*len(s):
            if s[0]=='+':
                s='-'*len(s[0:s.index('-')]) + s[s.index('-')+1:]
                ctr+=1
                continue

            if s[0]=='-':
                if '+' in s:
                    s='+'*len(s[0:s.index('+')]) + s[s.index('+')+1:]
                    ctr+=1
                else:
                    s='+'*len(s)
                    ctr+=1
        print "Case #" + str(i) + ": " + str(ctr)
        
panc(t)
