infile = open('input.txt', 'r')
outfile = open('output.txt', 'w')

def flipTo(n, s):
    result = ''
    for i in range(len(s)):
        if i <= n:
            flipped = '+'
            if s[n-i] == '+':
                flipped = '-'
            result += flipped
        else:
            result += s[i]
    return result

cases = int( infile.readline())
for case in range(1, cases+1):
    stack = infile.readline()[:-1]
    flips = 0
    lowestWrong = stack.rfind('-')
    while lowestWrong != -1:
        if stack[0] == '+':
            flips += 1
            stack = flipTo(stack.find('-')-1, stack)
        flips += 1
        stack = flipTo(lowestWrong, stack)

        lowestWrong = stack.rfind('-')

    outfile.write('Case #'+str(case)+': '+str(flips)+'\n')

infile.close()
outfile.close()
