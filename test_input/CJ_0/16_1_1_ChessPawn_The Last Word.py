fin = open("A-large.in",'r')
fout = open("A-large.out",'w')

def lastWord(inp,out=""):

    out2 = ""
    for c in inp:
        if out2 == "":
            out2+=c
        else:
            if c < out2[0]:
                out2+=c
            else:
                out2 = c+out2

    return out2
'''
    if inp=="":
        return out
    
    elif out == "":
        return lastWord(inp[1:],out+inp[0])
    else:
        nxt = inp[0]
        if nxt < out[0]:
            return lastWord(inp[1:],out+nxt)
        else:
            return lastWord(inp[1:],nxt+out)
'''
cases = int(fin.readline())

for c in range(cases):

    
    fout.write("Case #%d: %s\n" %(c+1, lastWord(fin.readline().strip())))

fin.close()
fout.close()
