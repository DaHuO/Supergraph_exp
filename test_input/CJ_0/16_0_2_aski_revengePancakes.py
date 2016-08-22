

def revPat(string, pos):
    string = reverseIt(string[:pos])+string[pos:]
    return string

def reverseIt(string):
    if len(string)==0:
        return ''
    if string[0] == '-':
        return '+'*len(string)
    else:
        return '-'*len(string)


# x = raw_input()
# print revPat(x, 1)
test = int(raw_input())


for i in range(test):
    pan_string = raw_input()
    count = 0
    for j in range(len(pan_string)-1):

        if pan_string[j] == pan_string[j+1]:
            continue
        else:
            count+=1
            pan_string = revPat(pan_string, j+1)

    if pan_string[0] == '-':
        print 'Case #'+str(i+1)+': '+str(count+1)
    else:
        print 'Case #'+str(i+1)+': '+str(count)
