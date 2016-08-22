'''
Created on 16 Apr 2016

@author: boom
'''

class LastWord():
    
    pass

def main():
    
    testFile = 'problem1A.txt'
    with open(testFile) as f:
        lineCount = 1
        next(f)
        for line in f:
            wordsList = list()
            string = line.rstrip('\n')
            word = list()
            for letter in string:
                if len(word) == 0:
                    word = letter
                    wordsList.append(word)
                    continue
                
                buff = wordsList
                buff = map(lambda x:x+letter, buff)
                wordsList = map(lambda x:letter+x, wordsList) + buff
                
            wordsList.sort()
            print "Case #" + str(lineCount) + ": " + wordsList[-1]
            
            lineCount = lineCount + 1
            if lineCount > 100 : break
            
if __name__ == '__main__':
    main()