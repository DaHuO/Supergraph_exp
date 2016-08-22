#Bill Zhang
#Counting Sheep
#Google Code Jam

def readFile():
    file = open('A-large.in', 'r')
    fileout = open('lastwordout.txt', 'w')
    num = int(file.readline())
    for n in range(num):
        x = file.readline()
        if n != num-1:
            fileout.write("Case #"+str(n+1)+": "+winningWord(x))
        else:
            fileout.write("Case #"+str(n+1)+": "+winningWord(x))

def winningWord(n):
    final = ""
    for c in n:
        if len(final) == 0:
            final += c
        else:
            if c < final[0]:
                final = final+c
            elif c >= final[0]:
                final = c+final
    return final

readFile()

#print(sleepTime(166))