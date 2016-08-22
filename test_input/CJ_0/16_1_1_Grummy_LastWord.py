inputFile = open("A-large.in")
outputFile = open("A-large.out", "w")

testCases = int(inputFile.readline())

for testCase in range(testCases):
    s = inputFile.readline().strip()
    word = [s[0]]
    s = s[1:]

    for letter in s:
        if letter < word[0]:
            word.append(letter)
        else:
            word.insert(0, letter)

    outputFile.write("Case #" + str(testCase + 1) + ": " + "".join(word) + "\n")

inputFile.close()
outputFile.close()
