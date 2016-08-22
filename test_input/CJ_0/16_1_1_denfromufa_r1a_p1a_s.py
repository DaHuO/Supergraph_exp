#from itertools import permutations
import sys
sys.setrecursionlimit(100000)
def nextwords(s):
    if len(s) <=1:
        yield s
    else:
        for perm in nextwords(s[:-1]):
            #for i in range(2):#len(s)):
                # nb elements[0:1] works in both string and list contexts
            #print(perm)
            yield max(perm + s[-1], s[-1] + perm)
    #for p in permutations(s):
    # if n==0:
    #     return []
    # else:
    #     print(n,s)
    #     return [[[s[0]]+nextwords(n-1,s[1:])],
    #             [nextwords(n-1,s[1:])+[s[0]]]]
with open(r"/home/dta/Downloads/jam/input.txt",mode='r') as f1:
    finput=f1.readlines()
T=int(finput[0])
with open(r"/home/dta/Downloads/jam/output.txt",mode='w') as f2:
    for x in range(1,T+1):
        s=finput[x].strip()
        y=nextwords(s)
        #print(y)
        f2.write("Case #{x}: {y}\n".format(x=x,y=max(y)))#''.join()


