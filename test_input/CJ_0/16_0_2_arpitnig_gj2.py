def main():
    f=open('input2.txt','r')
    n=int(f.readline())
    testcases=[]
    for i in range(n):
        t=f.readline().rstrip('\n')
#        print(calculate(t,0))
        testcases.append(calculate(t,0))
    fo=open('output2.txt','w+')
    for i in range(n):
        fo.write('Case #{0}: {1} \n'.format(i+1,testcases[i]))

def calculate(t,n):
#    print 't=',t,";n=",n
    if len(t)<1:
#        print 'Part1'
        return n
    elif len(t)==1 and t=='+':
#        print 'Part2'
        return n
    elif len(t)==1 and t=='-':
#        print 'Part3'
        return n+1
    elif len(t)>1:
        if t.rfind('-')>0 and t[0]=='+':
#            print 'Part41'
            s=list(t)
            j=0
            while t[j]=='+':
                s[j]='-'
                j=j+1
            t="".join(s)
            n=n+1
            r=flip(t[:t.rfind('-')+1][::-1])
#            print "RF",r
            return calculate(r,n+1)
        elif t.rfind('-')>0 and t[0]=='-':
#            print 'Part42'
#            print t[:t.rfind('-')+1][::-1]
            r=flip(t[:t.rfind('-')+1][::-1])
#            print "RF",r
            return calculate(r,n+1)
        elif t.rfind('-')==0:
#            print 'Part43'
            return n+1
        elif t.rfind('-')==-1:
#            print 'Part44'
            return n

def flip(s):
#    print "S",s
    t=list(s)
    for i in range(len(t)):
#        print t[i]
        if t[i]=='+':
            t[i]='-'
#            print 'plus',t[i]
        elif t[i]=='-':
            t[i]='+'
#            print 'minus',t[i]
#    print t
    s="".join(t)
#    print "T",s
    return s
        
if __name__=="__main__":
    main()