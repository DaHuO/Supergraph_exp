#Take a word and give the last
#of a alphabetic sorted list
def sort_word(word):
    resultWord = ""
    #Look over every letter
    for letter in word:
        #If word empty, just add letter
        if len(resultWord) == 0:
            resultWord += letter
        else:
            #Else add letter at beginning if letter is greater than
            #first letter, else at the end
            if (letter >= resultWord[0]):
                resultWord = letter + resultWord
            else:
                resultWord += letter
    return resultWord











def main():
    result = ""
    i = 1
    #Open the input file
    with open("A-large.in", 'r') as inputFile:
        testCasesNumber = inputFile.readline()
        #Read every case
        for word in inputFile:
            if (i <= int(testCasesNumber)):
                word = word.replace("\n", "")
                result += "Case #" + str(i) + ": "  + sort_word(word) + '\n'
            i += 1
    #Write result
    with open("output.txt", 'w') as outputFile:
        outputFile.write(result)


main()
