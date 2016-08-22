FILENAME = "A-large"

inpt = open(FILENAME + ".in")
outpt = open(FILENAME + ".out",'w')

i = 0

for line in inpt:
    if i > 0:
        word = line[:-1]
        best = word[0]
        for l in word[1:]:
            best = max(best + l, l + best)
        outpt.write("Case #" + str(i) + ": " + best + "\n")
    i += 1

outpt.close()
inpt.close()
