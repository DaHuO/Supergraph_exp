#source="C:\Users\manish\Desktop\cj\A-small-attempt0.in"
source="C:\Users\manish\Desktop\cj\A-large.in"
dest="C:\Users\manish\Desktop\cj\Output.txt"
fin=open(source)
fout=open(dest,'w')
t=fin.readline()
t=int(t)
for i in range(t):
    x = fin.readline()
    a = list(x)
    b = [a[0]]
    for k in range(1,len(a)):
        if a[k]>=b[0]:
            b.insert(0,a[k])
        else:
            b.append(a[k])
    b = ''.join(str(s) for s in b)
            
    fout.write("Case #"+str(i+1)+": "+b+"\n")

fin.close()
fout.close()
