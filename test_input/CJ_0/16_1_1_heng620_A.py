import re, sys
array = []
with open('A-large.in') as f:
    numCases = int(next(f).split()[0]) # read first line
    for line in f: # read rest of lines
        array.append([str(x) for x in line.split()][0])


print("numCases: " + str(numCases))
print(array)

def buildResult(s):
    ans = ""
    maxCharIndex = 0
    for index in range(len(s)):
        if s[index] >= s[maxCharIndex]:
            maxCharIndex = index
            ans = s[index] + ans
        else:
            ans += s[index]
    return ans

with open('output.txt', 'w') as out:
    for index, value in enumerate(array):
        result = buildResult(array[index])
        out.write(str("Case #" + str(index+1) + ": "))
        out.write(str(result))
        out.write('\n')
        print("Case #" + str(index+1) + ": " + str(result) )
