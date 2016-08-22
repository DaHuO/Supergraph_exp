import sys
sys.setrecursionlimit=100000

def flipstack(n,stack):
    g=0
    c=stack[0]
    for s in stack[1:]:
        if s!=c:
            c=s
            g+=1
    if c=="-":# and g>1:
        g+=1
    return g

with open(r"/home/dta/Downloads/jam/input.txt",mode='r') as f1:
    finput=f1.readlines()
T=int(finput[0])

if len(finput)!=(T+1):
    raise Exception("bad input file")
with open(r"/home/dta/Downloads/jam/output.txt",mode='w') as f2:
    for x in range(1,T+1):
        S=finput[x].strip()
        print(S)
        y=flipstack(0,S)
        f2.write("Case #{x}: {y}\n".format(x=x,y=y))