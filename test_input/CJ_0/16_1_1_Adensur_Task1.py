import sys
sys.setrecursionlimit(2000)
data=[]
with open ("A-large.in") as handle:
    T=int(handle.readline())
    for t in range(T):
        d=handle.readline().strip("\n")
        data.append(d)
data

x=["CAB", "BCA", "ACB", "BAC"]
sorted(x)
#every time we put the next letter on the board, we can search for last word in alphabetical order
def Solve(word):
    if len(word)>1:
        prev=Solve(word[:-1])
    else:
        prev=""
    last_char=word[-1:]
    variants=[last_char+prev,prev+last_char]
    variants.sort()
    return("".join(variants[-1:]))

n=1
with open("output.txt","w") as handle:
    for dat in data:
        res=Solve(dat)
        
        string="Case #%s: %s\n"%(n,res)
        handle.write(string)
        #print string
        n+=1
