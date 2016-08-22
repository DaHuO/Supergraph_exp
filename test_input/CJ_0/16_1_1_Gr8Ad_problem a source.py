tests = int(input())
for i in range(0, tests):
    line = input()
    letters = []
    for q in range(0, len(line)):
        letters.append(line[q])
        
    poss = [letters[0]]
    for w in range(1, len(letters)):
        newposs = []
        for u in range(0, len(poss)):
            new1 = poss[u] + letters[w]
            new2 = letters[w] + poss[u]
##            temp = []
##            temp.append(new1)
##            temp.append(new2)
##            temp.sort()
            newposs.append(new1)
            newposs.append(new2)
        poss = newposs
    poss.sort()
    print("Case #" + str(i+1) + ": " + poss[-1])

##import itertools
##tests = int(input())
##for i in range(0, tests):
##    line = input()
##    letters = []
##    for q in range(0, len(line)):
##        letters.append(line[q])
####    print(letters)
##    words = []
##    for word in itertools.permutations(letters):
##        words.append(word)
##    words.sort()
##    poss = [letters[0]]
##    for w in range(1, len(letters)):
##        newposs = []
##        for u in range(0, len(poss)):
##            new1 = poss[u] + letters[w]
##            new2 = letters[w] + poss[u]
##            newposs.append(new1)
##            newposs.append(new2)
##        poss = newposs
####    print(newposs)
##    newposs.sort()
####    print(newposs)
##    print("Case #" + str(i+1) + ": " + newposs[-1])










    
##    for e in range(0, len(words)):
##        print(len(words[e]))
##        print(words)
##        for r in range(0, len(words[e])):
##            print("r", r)
##            try:
##                if r-1 != -1:
##                    one = abs(letters.index(words[e][r]) - letters.index(words[e][r-1]))
##                    print(one)
##                    if one > 1:
##                        del words[e]
##            except IndexError:
##                print("in error")
##            try:
##                if r+1 != len(words[e])-1:
##                    two = abs(letters.index(words[e][r]) - letters.index(words[e][r+1]))
##                    print(two)
##                    if two > 1:
##                        del words[e]
##            except IndexError:
##                pass
            
##    print(words)
