import sys

with open(sys.argv[1], 'r') as f:
    next(f)
    case = 1

    for line in f:
        word = list(line.rstrip())

        lastword = []
        lastword.append(word.pop(0))
    
        for c in word:
            #print (lastword)
            if c >= lastword[0]:
                lastword.insert(0,c)
            else:
                lastword.append(c)

        print ("Case #%d: %s" % (case, "".join(lastword)))
        case = case + 1
