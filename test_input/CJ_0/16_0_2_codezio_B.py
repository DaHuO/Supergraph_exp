#source="C:\Users\manish\Desktop\cj\B-small-attempt0.in"
source="C:\Users\manish\Desktop\cj\B-large.in"
dest="C:\Users\manish\Desktop\cj\Output.txt"
fin=open(source)
fout=open(dest,'w')
t=fin.readline()
t=int(t)
for i in range(t):
    x = list(fin.readline().strip())
    lx = len(x)
    lp = x.count("+")
    ans = 0
    while lp!=lx:
        j = 0
        s = 0
        while x[j]=='-':
            s = 1
            x[j]='+'
            j=j+1
            if j>=lx:
                break
        if s==0:
            while x[j]=='+' and j<lx:
                s=1
                x[j]='-'
                j=j+1
                if j>=lx:
                    break
        if s==1:
            ans = ans+1
        lp = x.count('+')


    fout.write("Case #"+str(i+1)+": "+str(ans)+"\n")
fin.close()
fout.close()
