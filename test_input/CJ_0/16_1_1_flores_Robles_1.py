IN = open("in", 'r')
OUT = open("out", 'w+')

n = IN.readline()

for x in xrange(0, int(n)):
    word = IN.readline().rstrip()
    newword = ""
    for ch in word:
        if newword == "":
            newword = ch
        elif ch >= newword[0]:
            newword = ch + newword
        else:
            newword = newword + ch

    outline = "Case #" + str(x+1) + ": " +  newword + "\n"
    OUT.write(outline)


# Close opended files
IN.close()
OUT.close()
