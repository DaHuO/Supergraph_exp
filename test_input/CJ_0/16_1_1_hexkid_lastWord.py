'''
Created on 15 Apr 2016

@author: Andy
'''

def lastWord(word):
    '''
    '''
    result = word[0]
    for s in word[1:]:
        if s < result[0]:
            result += s
        else:
            result = s + result
    return result

if __name__ == '__main__':
    with open('problem.txt') as fp:
        noOfProblems = int(fp.readline().strip())
        with open('solution1a1.txt','w') as solution:
            for x in range(noOfProblems):
                result = lastWord(fp.readline().strip())
                answerLine = 'Case #{0}: {1}\n'.format(x+1,result)
                print answerLine
                solution.write(answerLine)
