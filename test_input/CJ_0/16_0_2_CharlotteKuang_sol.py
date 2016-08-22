import pdb
import sys

def flippingPancakes(cakes): 
    l = len(cakes)

    if l == 0: return 0

    count = 0
    pos = 0
    face = cakes[0]

    while True:
        face = cakes[pos]
        i = pos + 1
        while i < l:
            if cakes[i] != face: break
            i += 1
        if i == l: break

        pos = i
        count += 1
        face = "+" if face == "-" else "-" 

    return count if face == "+" else count + 1

if __name__ == "__main__":
    f = open(sys.argv[1], "r")
    
    content = (f.read()).split("\n")

    caseNum = int(content[0])

    for i in range(caseNum):
        case = content[i+1]
        print "Case #%i: %s" % (i+1, flippingPancakes(case))
