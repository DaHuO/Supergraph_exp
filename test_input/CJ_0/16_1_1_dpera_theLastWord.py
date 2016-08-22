# Daniele Perazzolo April 2016
# Code Jam 2016

def problem(word):
    lastWord = word[0]
    for letter in range(1, len(word)):
        if word[letter] >= lastWord[0]:
            lastWord = word[letter] + lastWord
        else:
            lastWord += word[letter]
    return lastWord


t = int(input())
for i in range(1, t + 1):
    S = input()
    print("Case #{}: {}".format(i, problem(S)))