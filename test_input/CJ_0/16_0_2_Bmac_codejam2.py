def read_words(afile):
    words = []
    for line in afile:
        words.append(line.strip())
    return words

filename = open('Untitled.txt', 'r')
T = filename.readline()
aList = read_words(filename)
y = 0

while y < len(aList):
    input = aList[y]
    flips = 0
    i = 0


    while i < len(input):

        if i == 0 and input[i] == '-':
            
            flips += 1
            while i < len(input) and input[i] == '-':
                i += 1
        elif input[i] == '+':
            pass
        elif input[i] == '-':

            flips += 2
            while i < len(input) and input[i] is '-':
                i += 1
        i += 1

    print "Case #" + str(y+1) + ": " + str(flips)
    y += 1
