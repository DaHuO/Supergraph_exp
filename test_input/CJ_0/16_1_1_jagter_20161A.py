ind = open("A-large.in", "r")
outd = open("A-large.out", "w")

T = int(ind.readline())

for i in range(1, T+1):
    S = ind.readline().strip()
    
    lastword = S[0]
    
    for j in range(1,len(S)):
        if S[j] < lastword[0]:
            lastword += S[j]
        else:
            lastword = S[j] + lastword[:]
        print lastword
    
    print("Case #"+str(i)+": "+lastword+"\n")
    outd.write("Case #"+str(i)+": "+lastword+"\n")

ind.close()
outd.close()

