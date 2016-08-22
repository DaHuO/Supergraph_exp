'''
Created on Apr 9, 2016

@author: david
'''
#f=open("exampleB.txt")
#f=open("B-small-attempt0.in")
f=open("B-large.in")

T=int(f.readline())
P=[]
for i in range(T):
    p = f.readline().strip()[::-1] #[x=='+' for x in f.readline().strip()[::-1]]
    P.append(p)

def solve(s):
    pre='+'
    c=0
    for d in s:
        if pre!=d:
            c += 1
        pre = d
    return c        
        
def solve2(s):
    return rec(s,True) 
  
def rec(s,c):
    #print(s,c)
    if len(s)==0: return 0
    if s[0]==c: return rec(s[1:], c)
    for i,v in enumerate(s):
        if v==c: 
            return 1+rec((s[i:]), not c)
    return 1
    
fRes = open("res.txt", "w")
case=0
for p in P:
    print("[{0}]".format(p))
    case+=1
    sol = solve(p)
    print("Case #{}: {}".format(case,sol))
    fRes.write("Case #{}: {}\n".format(case,sol))
        
fRes.close()