import math
f = open("C-test.txt","r")
o = open("C-small-answers.txt","w")
T = int(f.readline())

for t in range(1,T+1):
    #print("Case "+str(t))
    n = [int(x) for x in f.readline().split()]
    s = "1000000000000001"
    l = []
    while len(l) < 50:
        print(l)
        l1 = [int(s,10)]
        for base in range(2,11):
            x = int(s,base)
            for i in range(2,int(math.sqrt(x))):
                if x%i == 0:
                    l1.append(i)
                    break
            else:
                break
        else:
            l.append(l1)
        s = str(bin(int(s,2)+2)[2:])
    o.write("Case #"+str(t)+":\n")
    for i in l:
        for j in i:
            o.write(str(j)+" ")
        o.write("\n")
o.close()
