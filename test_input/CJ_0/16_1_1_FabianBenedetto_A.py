import pdb; #pdb.set_trace()

def finalword(teststring,i):
    wordright = list()
    wordleft = list()
    for letter in teststring:
        if not wordright:
            wordright.append(letter)
        elif not wordleft:
            if letter < wordright[0]:
                wordright.append(letter)
            else:
                wordleft.append(letter)
        else:
            if letter >= wordleft[-1]:
                wordleft.append(letter)
            else:
                wordright.append(letter)
    wordleft = sorted(wordleft,reverse=True)
    finalword = wordleft + wordright
    return "Case #" + str(i) + ": " + ''.join(finalword)

t = int(raw_input())
for i in xrange(1, t + 1):
    thestring = [s for s in raw_input().split(" ")]
    thestring = ''.join(thestring)
    print finalword(thestring,i)
