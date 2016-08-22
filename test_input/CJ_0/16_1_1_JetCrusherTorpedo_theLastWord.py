outFile = "output.out"
inFile = "A-large.in"


def lw(letters):
    outStr = None
    for l in letters:
        if outStr == None:
            outStr = l
            continue
        if l >= outStr[0]:
            outStr = l + outStr
        else:
            outStr += l
    return outStr
##    lg = len(letters)
##    lg2 = lg//2
##    l1 = letters[0]
##    lastSorted = None
##    permutations = unique_permutations(letters)
##    for perm in permutations:
####        if perm[lg2] != l1 and perm[lg-lg2] != l1:
####            continue
##        perm = "".join(perm)
##        if lastSorted == None:
##            lastSorted = perm
##        elif perm > lastSorted:
##            lastSorted = perm
##    return lastSorted
    

with open(inFile, "r") as f:
    with open(outFile, "w") as of:
        n = int(f.readline().strip("\n"))
        for i in range(n):
            string = f.readline().strip("\n")
            word = lw(string)
            of.write("Case #" + str(i+1) + ": " + word + "\n")
