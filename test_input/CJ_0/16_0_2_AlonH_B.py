f = open("B-large.in","r")
o = open("B-large-answers.txt","w")
T = int(f.readline())

for t in range(1,T+1):
    #print("Case "+str(t))
    n = f.readline()
    if n[-1] == '\n':
        n = n[:-1]
    l = len(n)
    #print(n)
    #n = [i == '+' for i in n]
    s = 0
    if n[l-1] == '-':
        s+=1
    l = len(n)
    for i in range(l-1):
        #print(i)
        if n[i] != n[i+1]:
            s += 1
    #print(s)
    #l = [int(x) for x in f.readline().split()]
    #o.write(n)
    o.write("Case #"+str(t)+": "+str(s)+"\n")
o.close()
