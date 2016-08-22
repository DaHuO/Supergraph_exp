fin = open("B-large.in",'r')
fout = open("B-large.out",'w')

numCases = int(fin.readline())

def myFn(s, opCount=0):
    if (s[0] == '+'):
        idx = s.find('-')
        if idx == -1:
            return opCount
        else:
            return myFn(('-'*idx)+s[idx:],opCount+1)
    else:
        idx = s.find('+')
        if idx == -1:
            return opCount+1
        else:
            return myFn(('+'*idx)+s[idx:],opCount+1)

for case in range(numCases):
    fout.write("Case #%d: %d\n" %(case+1, myFn(fin.readline().strip())))

fin.close()
fout.close()
    
        
