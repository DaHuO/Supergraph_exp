f = open("a.in")
fl = open("a.out","w")
t = int(f.readline().strip())
for i in range(1,t+1):
    s=f.readline().strip()
    L=[]
    ct=[]
    for m in range((2**(len(s)-1))):
        b=bin(m)[2:]
        while len(b) < len(s)-1:
            b = "0" * (len(s)-1 - len(b)) + b
        ct.append( b )
    while (len(L) != len(ct)) and len(s)>1:
        for j in ct:
            ind = 1
            string = s[0]
            for k in j:
                if k=='0':
                    string = s[ind] + string
                elif k=='1':
                    string += s[ind]
                if ind < len(s)-1:
                    ind+=1
            L.append(string)
    L.sort()
    if len(s)>1:
        res = L[len(L)-1]
    else:
        res = s
    fl.write("Case #"+str(i)+": "+res)
    fl.write("\n")
f.close()
fl.close()