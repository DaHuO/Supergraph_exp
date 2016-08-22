infile = open('input.txt', 'r')
outfile = open('output.txt', 'w')

cases = int( infile.readline() )
for case in range(cases):
    word = infile.readline()[:-1]
    sendLefts = []

    furthestRight = len(word)-1
    while furthestRight > 0:
        biggestSeen = 0
        for i in range(0, furthestRight+1):
            if word[i] >= word[biggestSeen]:
                biggestSeen = i
        sendLefts.insert(0, biggestSeen)
        furthestRight = biggestSeen-1
        

    lastWord = []
    for i in range(len(word)):
        if i in sendLefts:
            lastWord.insert(0, word[i])
        else:
            lastWord.append( word[i] )
    lastWord = ''.join(lastWord)

    outfile.write('Case #'+str(case+1)+': '+lastWord+'\n')

infile.close()
outfile.close()
        
