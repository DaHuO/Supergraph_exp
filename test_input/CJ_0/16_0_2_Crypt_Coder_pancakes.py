test=int(raw_input())
ti=0
while(test):
    test-=1
    ti+=1
    s=raw_input()
    length=len(s)
    pcnt=0
    mcnt=0
    prev=s[0]
    st=""
    st+=s[0]
    if(s[0]=='+'):
        pcnt+=1
        first=1
    else:
        mcnt+=1
        first=0
    for i in xrange(1,length):
        if(s[i]==prev):
            continue
        else:
            prev=s[i]
            st+=s[i]
            if(prev=='+'):
                pcnt+=1
            else:
                mcnt+=1
    if s[length-1]=='+':
        pcnt-=1
    temp="#"+str(ti)+":"
    print "Case",temp,
    if(pcnt==0 and mcnt==0):
        print "0"
        continue
    if(pcnt==0):
        print "1"
        continue
    if(mcnt==0):
        print "0"
        continue
    if(pcnt==1 and mcnt==1 and first):
        print "2"
        continue
    if(pcnt==1 and mcnt==1 and first==0):
        print "1"
        continue
    if(first):
        print 2*pcnt
        continue
    if(first==0):
        print 2*pcnt+1
        continue
