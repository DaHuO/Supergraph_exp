"""
    Author : NILESH AGARWAL
    Gmail : nilesh.kumpawat@gmail.com
"""

def find_lastword(s):
    s = list(s)
    d = []
    w = s[0]
    for x in s: 
        if w <= x:
            d.insert(0,x)
            w = x
        else:
            d.append(x)
    return "".join(d)

cases=0
filer = open('ia2.in')
filew = open('poa2.txt','w')
matrix = filer.read()
matrix = [item.split() for item in matrix.split('\n')[:-1]]
i = []
for u in matrix:
    i.extend(u)
cnt = 0
t = int(i[cnt])
cnt=cnt+1
for q in range(t):
    l = i[cnt]
    cnt=cnt+1
    cases = cases+1
    filew.write("Case #"+str(cases)+":"+" ")
    string = find_lastword(l)
    print string 
    filew.write(string+" \n")
filew.close()
filer.close()
