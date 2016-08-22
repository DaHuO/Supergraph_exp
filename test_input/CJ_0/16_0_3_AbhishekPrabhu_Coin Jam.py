import random
l=["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]
inpfile=open("C-large.txt","r")
outfile=open("outputfile1.txt","w")
outfile.write("Case #1:"+"\n")
T=int(inpfile.readline())
inp=(inpfile.readline()).split()
N=int(inp[0])
J=int(inp[1])
i=0
while(i<J):
    num="1"
    random.shuffle(l)
    for b in range(N-2):
        num=num+l[b]
    num=num+'1'
    out=str(num)
    print num
    f=0
    e=0
    for c in range(2,11,1):
        conv=int(num,c)
        e=e+1
        print e
        for d in [2,3,5,7,11,13,17,19,23,29,31,37,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199] :
            if conv%d==0 :
                out=out+" "+str(d)
                f=f+1
                break
        if f!=e :
            break
    if f==9 :
        print out
        outfile.write(out+"\n")
        outfile.flush()
        i=i+1
outfile.close()
inpfile.close()
