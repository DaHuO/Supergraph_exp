fobj = open(r"C:\Users\Ekansh\Downloads\B-large.in")
fout = open(r"C:\Users\Ekansh\Downloads\output21.txt","w")
n = 0
x1 = 1
for line in fobj:
    n = line.rstrip()
    break
for z in fobj:
    s = z.rstrip()
    s1 = []
    swaps = 0
    temp = len(s)-1
    for j in s:
        if j =="+":
            s1.append(1)
        else:
            s1.append(-1)
    while(True):
        if(s1[temp]==1 and temp>=0):
            temp -= 1
        else:
            break
    while(s1.count(1)!=len(s)):
        if(s1[0]==-1 and s1[temp]==-1):
            s1[0:temp+1] = s1[temp::-1]
            swaps += 1
            for i in range(temp+1):
                s1[i] = s1[i]*-1
            while(True):
                if(s1[temp]==1 and temp>=0):
                    temp -= 1
                else:
                    break
        elif(s1[0]==1 and s1[temp]==-1):
            x = temp-1
            while(True):
                if(s1[x]==-1):
                    x -= 1
                else:
                    break
            s1[0:x+1] = s1[x::-1]
            swaps += 1
            for i in range(x+1):
                s1[i] = s1[i]*-1
    abc = "Case #"+str(x1)+": "+str(swaps)+"\n"
    fout.write(abc)
    x1 += 1
fobj.close()
fout.close()
