lines = open("wordsin.txt").read().splitlines()
out = ""
for i in xrange(1,len(lines)):
    w = (lines[i])
    c = ""
    for j in w:
        if c == "":
            c=j
        elif j>=c[0]:
            c = j+c
        else:
            c = c+j
    out += "Case #"+str(i)+": "+c+"\n"
open("wordsout.txt","w").write(out)

    

