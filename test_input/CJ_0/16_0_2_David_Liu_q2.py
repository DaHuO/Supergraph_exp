inf=open("B-large.in", "r")
outf=open("q2.out", "w")

def f(s):
    t=""
    for c in s:
        if t=="" or c!=t[0]:
            t=c+t
    return len(t)-int(t[0]=="+")

TT=int(inf.readline())+1
for T in range(1, TT):
    s=inf.readline()
    s=s[:len(s)-1]
    outf.write("Case #{0}: {1}\n".format(T, f(s)))
inf.close()
outf.close()