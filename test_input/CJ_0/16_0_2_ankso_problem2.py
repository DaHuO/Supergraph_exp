

def reversePattern(string, pos):
    string = reverseThis(string[:pos])+string[pos:]
    return string

def reverseThis(string):
    if len(string)==0:
        return ''
    if string[0] == '-':
        return '+'*len(string)
    else:
        return '-'*len(string)


testCase = int(raw_input())


for i in range(testCase):
    sampleString = raw_input()
    count = 0
    for j in range(len(sampleString)-1):

        if sampleString[j] == sampleString[j+1]:
            continue
        else:
            count+=1
            sampleString = reversePattern(sampleString, j+1)

    if sampleString[0] == '-':
        print 'Case #'+str(i+1)+': '+str(count+1)
    else:
        print 'Case #'+str(i+1)+': '+str(count)
