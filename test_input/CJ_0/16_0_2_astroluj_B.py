
def isHappy (flipStack):

    happySideCount = 0
    for i in flipStack:
        if i == '+': happySideCount += 1
        else: break

    return happySideCount == len(flipStack)


def flip (flipStack, side, limitSize):
    
    for i in range(limitSize):
        flipStack[i] = side


    
# main
inputFile = open ('B-large.in', 'r')
outputFile = open('output.txt', 'w')

testCase = int(inputFile.readline())
for i in range(testCase):

    flipStack = [i for i in inputFile.readline().replace('\n', '')]
    answer = 0

    
    while not isHappy (flipStack):

        for idx, val in enumerate (flipStack):
            if (idx < (len(flipStack) - 1) and val != flipStack[idx + 1])\
               or idx == (len(flipStack) - 1):
                # flip
                flip (flipStack, ('+' if flipStack[idx] == '-' else '-'), idx + 1)
   
                break
                
        answer += 1
    else: outputFile.write('Case #{0}: {1}\n'.format(i + 1, answer))

    
inputFile.close()
outputFile.close()
