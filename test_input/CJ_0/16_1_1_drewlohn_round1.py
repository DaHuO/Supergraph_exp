import csv as csv

print 'Starting'

inFile = open('A-large (1).in','rb')
data = csv.reader(inFile,delimiter=' ')
numTests = int(data.next()[0])

outFile = open('outputSubmission.csv','wb')
outer = csv.writer(outFile)
##outString = 'Case #1:' 
##outer.writerow([outString])



def letterNum(letter):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    i = 0
    for val in letters:
        if letter == val:
            return i
        i += 1
    return 'none'


count = 0
for i in xrange(numTests):
    S = data.next()[0]
    previousStartNum = 0
    lastWord = ''
    for letter in S:
        loc = letterNum(letter.lower())
        if loc >= previousStartNum:
            lastWord = letter + lastWord
            previousStartNum = loc
        else:
            lastWord += letter
        
    print lastWord    
    outString = 'Case #' + str(i+1) + ': ' + lastWord
    outer.writerow([outString])

inFile.close()
outFile.close()
            
        

print 'Done'
