f = open("input.txt","r+")
fout = open("rounda1.txt","w+")
n = int(f.readline())
for j in xrange(n):
    s = f.readline()
    s = s.split("\n")
    s = s[0]
    print s,
    c = ['']*len(s)
    c[0] = s[0]
    for i in range(1,len(s)):
        if(s[i] >= c[0]):
            temp = c[0:i]
            c[0] = s[i]
            c[1:i+1] = temp
        else:
            c[i] = s[i]
    r = "Case #%d: "%(j+1)
    fout.write(r)
    for i in range (len(c)):
        #print c[i],
        temp = c[i]
        fout.write(temp)
    fout.write("\n")
f.close()
fout.close()
