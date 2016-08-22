def main():
    f=open('input1.txt','r')
    n=int(f.readline())
    testcases=[]
    for i in range(n):
        t=f.readline().rstrip('\n')
        testcases.append(calculate(t))
    fo=open('output1.txt','w+')
    for i in range(n):
        #print 'Case #{0}: {1}'.format(i+1,testcases[i])
        fo.write('Case #{0}: {1} \n'.format(i+1,testcases[i]))
#    print testcases

def calculate(t):
    s=[]
    s.insert(0,t[0])
#    print s
    for i in range(1,len(t)):
        l=len(s)
        for j in range(len(s)):
            x=s[j]
#            print t[i]+x
 #           print x+t[i]
            s.append(t[i]+x)
            s.append(x+t[i])
        s=s[l:len(s)]
    y=sorted(s)
    print y[-1]
    return y[-1]
    
if __name__=="__main__":
    main()
