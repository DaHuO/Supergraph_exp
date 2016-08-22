def ThePancakeRev(pancakes):
    cnt = sum(map(lambda i: pancakes[i] != pancakes[i+1], range(len(pancakes)-1)))
    return cnt + (pancakes[0]=='-' and (cnt%2)==0) + (pancakes[0]=='+' and (cnt%2)==1)

path = r'C:\Users\HOME\Downloads\CodeJam'
fileName = 'B-large.in'
inputPath = r'%s\in\%s' % (path, fileName)
outputPath = r'%s\out\%s' % (path, fileName.replace('.in', '.out'))

outputFile = open(outputPath, 'w')
inFile = open(inputPath, 'r')
inFile.next()
for i, line in enumerate(inFile):
    outputFile.write('Case #%s: %s\n' % (i+1, ThePancakeRev(line.strip())))
outputFile.close()