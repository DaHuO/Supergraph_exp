def aLastWord(word):
    newWord = ""

    for i in range(len(word)):
        char = word[i]

        if len(newWord) == 0:
            newWord = char
        else:
            if char < newWord[0]:
                newWord = newWord + char
            else:
                newWord = char + newWord


    return newWord


def main():

    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        word = aLastWord(raw_input())
        print ("Case #{}: {}".format(i, word))

if __name__=='__main__':
    main()