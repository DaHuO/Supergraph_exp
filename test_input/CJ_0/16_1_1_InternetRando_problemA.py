o = open('largeA.out', 'w')

with open('A-large.in', 'r') as i:
    counter = 1
    startNum = i.readline()
    for line in i:
        finalString = ''
        for letter in line:
            if len(finalString) == 0:
                finalString = letter
            elif letter >= finalString[0]:
                finalString = letter + finalString
            else:
                finalString = finalString + letter
        o.write('Case #' + str(counter) + ': ' + finalString)
        counter += 1

o.close()
