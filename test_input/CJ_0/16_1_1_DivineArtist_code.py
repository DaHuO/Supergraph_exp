inptr=open("A-large.in")
outptr=open("output.txt","w")

t=int(inptr.readline())
print t

for i in range(t):
    txt=inptr.readline()
    final=""
    for letter in txt:
        if final=="": final=letter
        else:
            if final[0]>letter:
                final=final+letter
            else:
                final=letter+final
    print final
    outptr.write("Case #"+str(i+1)+": "+final)
    